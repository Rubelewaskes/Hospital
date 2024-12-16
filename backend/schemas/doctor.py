from pydantic import BaseModel
from typing import List
from sqlalchemy.dialects.postgresql import UUID
import uuid

from auth.schemas import UserCreate
from .area import AreaSchema


class DoctorSchema(BaseModel):
    id: int
    first_name: str
    second_name: str
    third_name: str
    phone_number: str
    experience: int
    user_id: uuid.UUID


class DoctorSchemaAdd(BaseModel):
    first_name: str
    second_name: str
    third_name: str
    phone_number: str
    experience: int
    areas_list: List[AreaSchema]
    user_create: UserCreate

class DoctorSchemaUpd(BaseModel):
    id: int
    first_name: str
    second_name: str
    third_name: str
    phone_number: str
    experience: int
    areas_list: List[AreaSchema]