from pydantic import BaseModel
from typing import List

from .area import AreaSchema


class DoctorSchema(BaseModel):
    id: int
    first_name: str
    second_name: str
    third_name: str
    phone_number: str
    experience: int


class DoctorSchemaAdd(BaseModel):
    first_name: str
    second_name: str
    third_name: str
    phone_number: str
    experience: int
    areas_list: List[AreaSchema]

class DoctorSchemaUpd(BaseModel):
    id: int
    first_name: str
    second_name: str
    third_name: str
    phone_number: str
    experience: int
    areas_list: List[AreaSchema]