from pydantic import BaseModel

class AreaDoctorSchema(BaseModel):
    id: int
    doctor_id: int
    area_id: int
