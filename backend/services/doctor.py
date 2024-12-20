from utils.repository import AbstractRepository
from fastapi import HTTPException

from models import Doctor, AreaDoctor


class DoctorService:
    def __init__(self, doctor_repo: AbstractRepository):
        self.doctor_repo: AbstractRepository = doctor_repo()
    
    async def get_one_doctor(self, id):
        one_doctor = await self.doctor_repo.find_one(id)
        return one_doctor

    async def get_all_doctors(self):
        all_doctors = await self.doctor_repo.get_all_doctors()
        return all_doctors
    
    async def update_doctor(self, data):
        id = data.id
        updatedDoctor = {
            "first_name": data.first_name,
            "second_name": data.second_name,
            "third_name": data.third_name,
            "phone_number": data.phone_number,
            "experience": data.experience,
        }

        areas_list = []
        for area in data.areas_list:
            areas_list.append(AreaDoctor(area_id=area.id, doctor_id=data.id))
        
        if updated_doctor := await self.doctor_repo.update_doctor(id, updatedDoctor, areas_list):
            return updated_doctor

    async def add_one_doctor(self, data):
        newUser = data.user_create

        newDoctor = Doctor(
            first_name=data.first_name, second_name=data.second_name,
            third_name=data.third_name, phone_number=data.phone_number, 
            experience=data.experience,)

        areas_list = []
        for area in data.areas_list:
            areas_list.append(AreaDoctor(area_id=area.id))

        if added_doctor := await self.doctor_repo.add_new_doctor(newDoctor, areas_list, newUser):
            return added_doctor

        raise HTTPException(
                status_code=418,
                detail="Insertation error, invalid value"
            )