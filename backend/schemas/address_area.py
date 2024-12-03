from pydantic import BaseModel

class AddressAreaSchema(BaseModel):
    id: int
    street: str
    house: str
    building: str
    flat: int
    area_id: int