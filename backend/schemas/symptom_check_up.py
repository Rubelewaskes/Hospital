from pydantic import BaseModel

class SymptomCheckUpSchema(BaseModel):
    id: int
    symptom_id: int
    check_up_id:int
    description: str