from utils.repository import AbstractRepository


class PatientService:
    def __init__(self, patient_repo: AbstractRepository):
        self.patient_repo: AbstractRepository = patient_repo()

    async def get_all_patients(self):
        patient = await self.patient_repo.find_all()
        return patient
    
    async def get_one_patient(self, id):
        patient = await self.patient_repo.find_one(id)
        return patient
    
