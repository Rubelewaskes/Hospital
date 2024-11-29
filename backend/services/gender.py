from utils.repository import AbstractRepository


class GenderService:
    def __init__(self, patient_repo: AbstractRepository):
        self.patient_repo: AbstractRepository = patient_repo()

    async def get_all_genders(self):
        gender = await self.patient_repo.find_all()
        return gender
    
