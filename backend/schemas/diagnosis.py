from pydantic import BaseModel

class DiagnosisSchemaAdd(BaseModel):
    name: str

class DiagnosisSchema(BaseModel):
    id: int
    name: str