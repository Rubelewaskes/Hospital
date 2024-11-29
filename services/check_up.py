from utils.repository import AbstractRepository


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

    async def get_all_symptoms(self, id):
        get_all_symptoms = await self.check_up_repo.get_all_symptoms(id)
        return get_all_symptoms