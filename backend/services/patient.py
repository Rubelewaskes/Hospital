from utils.repository import AbstractRepository
from fastapi import HTTPException 

from models import Patient

from services import AddressService
from repositories.address import AddressAreaRepository


class PatientService:    
    def __init__(self, patient_repo: AbstractRepository):
        self.patient_repo: AbstractRepository = patient_repo()

    async def get_all_patients(self):
        patient = await self.patient_repo.find_all()
        return patient
    
    async def get_one_patient(self, id):
        patient = await self.patient_repo.find_one(id)
        return patient

    async def get_all_patients_on_doctor_area(self, id):
        all_patients_on_doctor_area = await self.patient_repo.get_all_patients_on_doctor_area(id)
        return all_patients_on_doctor_area

    async def add_new_patient(self, data):
        address_info = data.address
        
        address_service = AddressService(AddressAreaRepository)
        
        if address_id := await address_service.get_address_id(address_info):
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

       
