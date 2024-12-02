from utils.repository import AbstractRepository
from fastapi import HTTPException 

from models.area import AddressArea
from models.patient import Patient


class PatientService:    
    def __init__(self, patient_repo: AbstractRepository, address_repo: AbstractRepository):
        self.patient_repo: AbstractRepository = patient_repo()
        self.address_repo: AbstractRepository = address_repo()

    async def get_all_patients(self):
        patient = await self.patient_repo.find_all()
        return patient
    
    async def get_one_patient(self, id):
        patient = await self.patient_repo.find_one(id)
        return patient

    async def add_new_patient(self, data):
        address_info = AddressArea(street=data.address.street, house=data.address.house, 
            building=data.address.building, flat=data.address.flat)
        if address_id := await self.address_repo.find_address(address_info):
            print(address_id)
            new_patient_info = Patient(
                first_name=data.first_name, 
                second_name=data.second_name, 
                third_name=data.third_name, 
                phone_number=data.phone_number, 
                address_id=address_id["address_id"], 
                born_date=data.born_date, 
                gender_id=data.gender_id,
            )
            if patient := await self.patient_repo.add_one(new_patient_info):
                return patient
            raise HTTPException(
                status_code=404,
                detail="Address not found"
            )
        raise HTTPException(
                status_code=400,
                detail="Adding error"
            )

       
