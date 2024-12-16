from datetime import date
from pydantic import BaseModel
from auth.schemas import UserCreate
from sqlalchemy.dialects.postgresql import UUID
import uuid


class PatientSchema(BaseModel):
    id: int
    first_name: str
    second_name: str
    third_name: str
    phone_number: str
    address_id: int
    born_date: date
    gender_id: int
    user_id: uuid.UUID

    class Config:
        from_attributes = True

class AddressSchema(BaseModel):
    street: str
    house: str | None
    building: str | None
    flat: int | None

class PatientSchemaAdd(BaseModel):
    first_name: str
    second_name: str
    third_name: str
    phone_number: str
    born_date: date
    gender_id: int
    address: AddressSchema
    user_create: UserCreate

class PatientSchemaUpd(BaseModel):
    id: int
    first_name: str
    second_name: str
    third_name: str
    phone_number: str
    born_date: date
    gender_id: int
    address: AddressSchema