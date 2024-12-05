from pydantic import BaseModel
from typing import Optional

class AddressAreaSchema(BaseModel):
    id: int
    street: str
    house: Optional[str] = None 
    building: Optional[str] = None 
    flat: Optional[int] = None 
    area_id: int

class AddressAreaSchemaAdd(BaseModel):
    street: str
    house: Optional[str] = None 
    building: Optional[str] = None 
    flat: Optional[int] = None 
    area_id: int