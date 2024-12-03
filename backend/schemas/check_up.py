from typing import List, Optional
from datetime import datetime

from pydantic import BaseModel

class CheckUpSchema(BaseModel):
    id: int
    check_up_place_id: int
    check_up_date: datetime
    doctor_id: int
    patient_id: int
    diagnosis_id: int
    prescription: str

class SymptomCheckUpAddSchema(BaseModel):
    check_up_id: Optional[int] = None
    symptom_id: Optional[int] = None
    description: Optional[str] = None

class CheckUpAddSchema(BaseModel):
    check_up_place_id: int
    check_up_date: datetime
    doctor_id: int
    patient_id: int
    diagnosis_id: Optional[int] = None
    prescription: Optional[str] = None
    symptoms_list: List[SymptomCheckUpAddSchema]