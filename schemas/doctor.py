from datetime import date

from pydantic import BaseModel


class DoctorSchema(BaseModel):
    id: int
    first_name: str
    second_name: str
    third_name: str
    phone_number: str
    experience: int
