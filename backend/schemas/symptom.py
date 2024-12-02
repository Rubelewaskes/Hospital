from pydantic import BaseModel

class SymptomSchema(BaseModel):
    id: int
    name: str