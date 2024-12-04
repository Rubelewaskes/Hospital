from utils.repository import AbstractRepository

from models import Doctor, AreaDoctor


class DoctorService:
    def __init__(self, doctor_repo: AbstractRepository):
        self.doctor_repo: AbstractRepository = doctor_repo()

    async def add_one_doctor(self, data):
        newDoctor = Doctor(
            first_name=data.first_name, second_name=data.second_name,
            third_name=data.third_name, phone_number=data.phone_number, 
            experience=data.experience,)

        areas_list = []
        for area in data.areas_list:
            areas_list.append(AreaDoctor(area_id=area.id))

        if added_doctor := await self.doctor_repo.add_new_doctor(newDoctor, areas_list):
            return added_doctor

        raise HTTPException(
                status_code=418,
                detail="Insertation error, invalid value"
            )