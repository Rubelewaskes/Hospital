from utils.repository import AbstractRepository


class SymptomService:
    def __init__(self, symptom_repo: AbstractRepository):
        self.symptom_repo: AbstractRepository = symptom_repo()

    async def get_all_symptoms(self):
        all_symptoms = await self.symptom_repo.find_all()
        return all_symptoms