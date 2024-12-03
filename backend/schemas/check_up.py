from datetime import date

from pydantic import BaseModel

class CheckUpSchema(BaseModel):
    id: int
    check_up_place_id: int
    check_up_date: date
    doctor_id: int
    patient_id: int
    diagnosis_id: int
    prescription: str