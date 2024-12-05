from utils.repository import AbstractRepository

from models import Diagnosis


class DiagnosisService:
    def __init__(self, diagnosis_repo: AbstractRepository):
        self.diagnosis_repo: AbstractRepository = diagnosis_repo()

    async def get_all_diagnosis(self):
        all_diagnoses = await self.diagnosis_repo.find_all()
        return all_diagnoses
    
    async def update_diagnosis(self, diagnosis):
        id = diagnosis.id
        updatedDiagnosis = {"name": diagnosis.name}
        if updated_diagnosis := await self.diagnosis_repo.update_one(id, updatedDiagnosis):
            return updated_diagnosis
        raise HTTPException(
                status_code=400,
                detail="Insert error"
            ) 

    async def add_one_diagnosis(self, diagnosis):
        newDiagnosis = Diagnosis(name=diagnosis.name)
        added_diagnosis = await self.diagnosis_repo.add_one(newDiagnosis)
        return added_diagnosis