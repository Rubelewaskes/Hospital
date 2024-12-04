from pydantic import BaseModel

class CheckUpPlaceSchema(BaseModel):
    id: int
    place: str

