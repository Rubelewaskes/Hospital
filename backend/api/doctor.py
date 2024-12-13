from typing import Annotated
from fastapi import APIRouter, Depends

from api.dependencies import doctor_service
from schemas import DoctorSchemaUpd, DoctorSchemaAdd
from services.doctor import DoctorService

from auth.users import  current_active_user
from auth.db import User

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
    user: User = Depends(current_active_user),
):
    if user.is_superuser:
        all_doctors = await doctor_service.get_all_doctors()
        response.headers["X-Total-Count"] = str(len(diagnoses))

        if _limit != 0:
            start = (_page - 1) * _limit
            end = start + _limit

            return diagnoses[start:end]
        return all_doctors

    raise HTTPException(
            status_code=403,
            detail="Forbidden"
        )


@router.post("/add_new")
async def add_new_doctor(
    doctor: DoctorSchemaAdd, 
    doctor_service: Annotated[DoctorService, Depends(doctor_service)],
    user: User = Depends(current_active_user),
):
    if user.is_superuser:
        added_doctor = await doctor_service.add_one_doctor(doctor)
        return added_doctor

    raise HTTPException(
            status_code=403,
            detail="Forbidden"
        )

@router.put("/update")
async def update_doctor(
    doctor: DoctorSchemaUpd, 
    doctor_service: Annotated[DoctorService, Depends(doctor_service)],
    user: User = Depends(current_active_user),
):
    if user.is_superuser:
        upd_doctor = await doctor_service.update_doctor(doctor)
        return upd_doctor

    raise HTTPException(
            status_code=403,
            detail="Forbidden"
        )