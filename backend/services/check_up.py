from utils.repository import AbstractRepository

from models.check_up import Diagnosis


class CheckUpService:
    def __init__(self, check_up_repo: AbstractRepository):
        self.check_up_repo: AbstractRepository = check_up_repo()
    
    # async def get_all_patients(self):
    #     patient = await self.patient_repo.find_all()
    #     return patient
    
    async def get_all_short_checkup(self, id):
        all_short_checkup = await self.check_up_repo.get_all_short_checkup(id)
        return all_short_checkup
    
    async def get_check_up(self, id):
        get_check_up = await self.check_up_repo.get_check_up(id)
        return get_check_up

    async def get_all_symptoms(self):
        all_symptoms = await self.check_up_repo.find_all()
        return all_symptoms
    
    async def get_all_check_up_places(self):
        check_up_places = await self.check_up_repo.find_all()
        return check_up_places
    
    async def get_all_patients_on_doctor_area(self, id):
        all_patients_on_doctor_area = await self.check_up_repo.get_all_patients_on_doctor_area(id)
        return all_patients_on_doctor_area

    async def add_one_diagnosis(self, diagnosis):
        newDiagnosis = Diagnosis(name=diagnosis.name)
        added_diagnosis = await self.check_up_repo.add_one(newDiagnosis)
        return added_diagnosis