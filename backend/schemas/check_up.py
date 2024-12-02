from datetime import date

from pydantic import BaseModel

class DiagnosisSchemaAdd(BaseModel):
    name: str

class CheckUpSchema(BaseModel):
    id: int
    check_up_place_id: int
    check_up_date: date
    doctor_id: int
    patient_id: int
    diagnosis_id: int
    prescription: str


class CheckUpPlaceSchema(BaseModel):
    id: int
    place: str


class DiagnosisSchema(BaseModel):
    id: int
    name: str

class SymptomSchema(BaseModel):
    id: int
    name: str

class SymptomCheckUpSchema(BaseModel):
    id: int
    symptom_id: int
    check_up_id:int
    description: str


