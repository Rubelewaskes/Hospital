from utils.repository import AbstractRepository

from models import SymptomCheckUp, Symptom

class SymptomService:
    def __init__(self, symptom_repo: AbstractRepository):
        self.symptom_repo: AbstractRepository = symptom_repo()

    async def get_all_symptoms(self):
        all_symptoms = await self.symptom_repo.find_all()
        return all_symptoms

    async def add_new_symptom(self, symptom):
        newSymptom = Symptom(name=symptom.name)
        if added_symptom := await self.symptom_repo.add_one(newSymptom):
            return added_symptom
        raise HTTPException(
                status_code=400,
                detail="Insert error"
            ) 
    
    async def update_symptom(self, symptom):
        id = symptom.id
        updatedSymptom = {"name": symptom.name}
        if updated_symptom := await self.symptom_repo.update_one(id, updatedSymptom):
            return updated_symptom
        raise HTTPException(
                status_code=400,
                detail="Insert error"
            ) 
            
    async def add_new_symptom_check_up(self, data):
        new_symptom_check_up_info = SymptomCheckUp(
            check_up_id=data.check_up_id, 
            symptom_id=data.symptom_id, 
            description=data.description)
        if symptom_check_up := await self.symptom_repo.add_one(new_symptom_check_up_info):
            return 
        raise HTTPException(
                status_code=400,
                detail="Insert error"
            ) 