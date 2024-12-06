from typing import List, Optional
from datetime import datetime

from pydantic import BaseModel, validator

class CheckUpSchema(BaseModel):
    id: int
    check_up_place_id: int
    check_up_date: datetime
    doctor_id: int
    patient_id: int
    diagnosis_id: int
    prescription: str

class SymptomCheckUpAddSchema(BaseModel):
    symptom_id: Optional[int] = None
    description: Optional[str] = None

class CheckUpSchemaAdd(BaseModel):
    check_up_place_id: int
    check_up_date: str
    doctor_id: int
    patient_id: int
    diagnosis_id: Optional[int] = None
    prescription: Optional[str] = None
    symptoms_list: List[SymptomCheckUpAddSchema]

    @validator('check_up_date')
    def parse_check_up_date(cls, v):
        return datetime.strptime(v, '%d.%m.%Y %H:%M:%S')