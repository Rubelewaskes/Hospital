from datetime import date

from pydantic import BaseModel


class PatientSchema(BaseModel):
    id: int
    first_name: str
    second_name: str
    third_name: str
    phone_number: str
    address_id: int
    born_date: date
    gender_id: int

    class Config:
        from_attributes = True
