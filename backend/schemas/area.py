from pydantic import BaseModel


class AreaSchema(BaseModel):
    id: int

class AddressAreaSchema(BaseModel):
    id: int
    street: str
    house: str
    building: str
    flat: int
    area_id: int

class AreaDoctorSchema(BaseModel):
    id: int
    doctor_id: int
    area_id: int

