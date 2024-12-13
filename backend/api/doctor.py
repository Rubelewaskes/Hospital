from typing import Annotated
from fastapi import APIRouter, Depends, Query, Response

from api.dependencies import doctor_service
from schemas import DoctorSchemaUpd, DoctorSchemaAdd
from services.doctor import DoctorService

router = APIRouter(
    prefix="/doctor",
    tags=["Doctor"],
)

@router.get("/get_all")
async def get_all_doctors(
    doctor_service: Annotated[DoctorService, Depends(doctor_service)],
    response: Response,
    _limit: int = Query(0, ge=0),
    _page: int = Query(1, ge=1),
):
    all_doctors = await doctor_service.get_all_doctors()
    response.headers["X-Total-Count"] = str(len(all_doctors))

    if _limit != 0:
        start = (_page - 1) * _limit
        end = start + _limit

        return all_doctors[start:end]
    return all_doctors

@router.post("/add_new")
async def add_new_doctor(
    doctor: DoctorSchemaAdd, 
    doctor_service: Annotated[DoctorService, Depends(doctor_service)],
):
    added_doctor = await doctor_service.add_one_doctor(doctor)
    return added_doctor

@router.put("/update")
async def update_doctor(
    doctor: DoctorSchemaUpd, 
    doctor_service: Annotated[DoctorService, Depends(doctor_service)],
):
    upd_doctor = await doctor_service.update_doctor(doctor)
    return upd_doctor