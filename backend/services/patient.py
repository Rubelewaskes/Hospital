from utils.repository import AbstractRepository
from fastapi import HTTPException 

from models import Patient

from services.address import AddressService
from repositories.address import AddressAreaRepository


class PatientService:    
    def __init__(self, patient_repo: AbstractRepository):
        self.patient_repo: AbstractRepository = patient_repo()

    async def get_all_patients(self):
        patient = await self.patient_repo.get_all_full()
        return patient
    
    async def update_patient(self, patient):
        id = patient.id

        address_info = patient.address
        address_service = AddressService(AddressAreaRepository)
        if address_id := await address_service.get_address_id(address_info):
            updatedPatient = {
                "first_name":patient.first_name, 
                "second_name":patient.second_name, 
                "third_name":patient.third_name, 
                "phone_number":patient.phone_number, 
                "born_date":patient.born_date, 
                "address_id":address_id["address_id"], 
                "gender_id":patient.gender_id,
            }

            if updated_patient := await self.patient_repo.update_one(id, updatedPatient):
                return updated_patient

            raise HTTPException(
                    status_code=400,
                    detail="update error"
                ) 

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

       
