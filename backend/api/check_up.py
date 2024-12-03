from typing import Annotated

from fastapi import APIRouter, Depends

from api.dependencies import check_up_service
from services.check_up import CheckUpService


router = APIRouter(
    prefix="/check_up",
    tags=["Check_up"],
)

@router.get("/get_all_checkups_of/{patient_id}")
async def get_all_check_ups_of_patient(
    patient_id: int,
    check_up_service: Annotated[CheckUpService, Depends(check_up_service)],
):
    check_ups = await check_up_service.get_all_short_checkup(patient_id)
    return check_ups

@router.get("/get_check_up/{check_up_id}")
async def get_check_up(
    check_up_id: int,
    check_up_service: Annotated[CheckUpService, Depends(check_up_service)],
):
    check_ups = await check_up_service.get_check_up(check_up_id)
    return check_ups




