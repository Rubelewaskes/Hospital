from utils.repository import AbstractRepository

from models import Diagnosis


class DiagnosisService:
    def __init__(self, diagnosis_repo: AbstractRepository):
        self.diagnosis_repo: AbstractRepository = diagnosis_repo()

    async def add_one_diagnosis(self, diagnosis):
        newDiagnosis = Diagnosis(name=diagnosis.name)
        added_diagnosis = await self.diagnosis_repo.add_one(newDiagnosis)
        return added_diagnosis