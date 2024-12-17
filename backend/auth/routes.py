from fastapi import Depends, FastAPI, APIRouter, HTTPException, Query, Response

from auth.db import User, create_db_and_tables
from auth.service import AuthService
from auth.users import  current_active_user, fastapi_users

from api.dependencies import doctor_service, patient_service, check_up_service

router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)

service = AuthService()

@router.get("/get_role")
async def get_user_role(user: User = Depends(current_active_user)):
    if user.is_superuser:
        return {"message": f"Hello Admin {user.email}!"}
    if user.is_doctor:
        return {"message": f"Hello Doctor {user.email}!"}
    else:
        return {"message": f"Hello Patient {user.email}!"}

@router.get("/get_me")
async def get_user_info(user: User = Depends(current_active_user)):
    if user.is_superuser:
        return {"email": user.email}
    elif user.is_doctor:
        doctor_id = await service.get_doctor_id(user.id)
        local_doctor_service = doctor_service()
        doctor_info = await local_doctor_service.get_one_doctor(doctor_id)
        return doctor_info
    elif user:
        patient_id = await service.get_patient_id(user.id)
        local_patient_service = patient_service()
        patient_info = await local_patient_service.get_one_patient(user.id)
        return patient_info

    raise HTTPException(
            status_code=403,
            detail="Forbidden"
        )
    
@router.get("/get_my_check_ups")
async def get_patient_check_ups(response: Response,
    _limit: int = Query(0, ge=0),
    _page: int = Query(1, ge=1),
    user: User = Depends(current_active_user)
):
    if not user.is_superuser and not user.is_doctor:
        patient_id = await service.get_patient_id(user.id)
        local_check_up_service = check_up_service()
        check_ups = await local_check_up_service.get_all_short_checkup(patient_id)

        response.headers["X-Total-Count"] = str(len(patient_id))
        
        if _limit != 0:
            start = (_page - 1) * _limit
            end = start + _limit

            return check_ups[start:end]
        return check_ups

    raise HTTPException(
            status_code=403,
            detail="Forbidden"
        )

@router.get("/get_my_patients")
async def get_doctor_patients(response: Response,
    _limit: int = Query(0, ge=0),
    _page: int = Query(1, ge=1),
    user: User = Depends(current_active_user)
):
    if user.is_doctor:
        doctor_id = await service.get_doctor_id(user.id)
        local_patient_service = patient_service()
        patients_info = await local_patient_service.get_all_patients_on_doctor_area(doctor_id)

        response.headers["X-Total-Count"] = str(len(patients_info))

        if _limit != 0:
            start = (_page - 1) * _limit
            end = start + _limit

            return patients_info[start:end]
        return patients_info

    raise HTTPException(
            status_code=403,
            detail="Forbidden"
        )

@router.delete("/delete_doctor")
async def make_doctor_unactive(id: int, user: User = Depends(current_active_user)):
    if user.is_superuser:
        doctor_uid = await service.get_doctor_uid(id)
        await service.unactivate(doctor_uid)
        return {"doctor_deactivated": id}

    raise HTTPException(
            status_code=403,
            detail="Forbidden"
        )


@router.delete("/delete_patient")
async def make_patient_unactive(id: int, user: User = Depends(current_active_user) ):
    if user.is_superuser:
        patient_uid = await service.get_patient_uid(id)
        await service.unactivate(patient_uid)
        return {"patient_deactivated": id}

    raise HTTPException(
            status_code=403,
            detail="Forbidden"
        )