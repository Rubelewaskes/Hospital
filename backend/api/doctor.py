from typing import Annotated
from fastapi import APIRouter, Depends

from api.dependencies import doctor_service
from schemas import DoctorSchemaAdd
from services.doctor import DoctorService

router = APIRouter(
    prefix="/doctor",
    tags=["Doctor"],
)

@router.post("/add_new")
async def add_new_doctor(
    doctor: DoctorSchemaAdd, 
    doctor_service: Annotated[DoctorService, Depends(doctor_service)],
):
    added_doctor = await doctor_service.add_one_doctor(doctor)
    return added_doctor