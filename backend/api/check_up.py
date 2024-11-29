from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException 

from api.dependencies import (check_up_service, 
check_up_place_service, 
symptom_service, 
)

from services.check_up import CheckUpService

router = APIRouter(
    prefix="/check_up",
    tags=["Check_ups"],
)

@router.get("/get_all_checkups_of/{user_id}")
async def get_all_check_ups(
    user_id: int,
    check_up_service: Annotated[CheckUpService, Depends(check_up_service)],
):
    check_ups = await check_up_service.get_all_short_checkup(user_id)
    return check_ups

@router.get("/get_check_up/{check_up_id}")
async def get_all_check_ups(
    check_up_id: int,
    check_up_service: Annotated[CheckUpService, Depends(check_up_service)],
):
    check_ups = await check_up_service.get_check_up(check_up_id)
    return check_ups

@router.get("/get_symptoms")
async def get_all_symptoms(
    check_up_service: Annotated[CheckUpService, Depends(symptom_service)],
):
    symptoms = await check_up_service.get_all_symptoms()
    return symptoms

@router.get("/get_check_up_places")
async def get_check_up_places(
    check_up_service: Annotated[CheckUpService, Depends(check_up_place_service)],
):
    symptoms = await check_up_service.get_all_check_up_places()
    return symptoms

@router.get("/get_all_patients_of_doctor/{doctor_id}")
async def get_check_up_places(
    doctor_id: int,
    check_up_service: Annotated[CheckUpService, Depends(check_up_service)],
):
    patients = await check_up_service.get_all_patients_on_doctor_area(doctor_id)
    return patients