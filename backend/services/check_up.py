from utils.repository import AbstractRepository

from models import CheckUp, SymptomCheckUp
from services.symptom import SymptomService
from repositories.symptom import SymptomRepository

class CheckUpService:
    def __init__(self, check_up_repo: AbstractRepository):
        self.check_up_repo: AbstractRepository = check_up_repo()
    
    async def get_all_short_checkup(self, id):
        all_short_checkup = await self.check_up_repo.get_all_short_checkup(id)
        for checkup in all_short_checkup:
            checkup["check_up_date"] = checkup["check_up_date"].strftime('%d.%m.%Y %H:%M:%S')
        return all_short_checkup
    
    async def get_check_up(self, id):
        get_check_up = await self.check_up_repo.get_check_up(id)
        get_check_up["check_up_date"] = get_check_up["check_up_date"].strftime('%d.%m.%Y %H:%M:%S')
        return get_check_up
    
    async def get_all_check_up_places(self):
        check_up_places = await self.check_up_repo.find_all()
        return check_up_places
    
    async def add_new_check_up(self, data):
        new_check_up_info = CheckUp(
            check_up_place_id=data.check_up_place_id, 
            check_up_date=data.check_up_date, 
            doctor_id=data.doctor_id, 
            patient_id=data.patient_id, 
            diagnosis_id=data.diagnosis_id, 
            prescription=data.prescription)

        symptoms_list = []
        for symptom in data.symptoms_list:
            symptoms_list.append(SymptomCheckUp(
                symptom_id=symptom.symptom_id, 
                description=symptom.description,
                ))    

        if check_up_id := await self.check_up_repo.add_new_check_up(new_check_up_info, symptoms_list):
            return check_up_id
        
        raise HTTPException(
                status_code=418,
                detail="Insertation error, invalid value"
            )
