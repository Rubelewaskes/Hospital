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

    class Config:
        from_attributes = True