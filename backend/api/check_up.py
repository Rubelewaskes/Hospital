from typing import Annotated
from fastapi import APIRouter, Depends, Query, Response

from api.dependencies import check_up_service
from services import CheckUpService
from schemas import CheckUpSchemaAdd


router = APIRouter(
    prefix="/check_up",
    tags=["Check_up"],
)

@router.get("/get_all_checkups_of/{patient_id}")
async def get_all_check_ups_of_patient(
    patient_id: int,
    check_up_service: Annotated[CheckUpService, Depends(check_up_service)],
    response: Response,
    _limit: int = Query(0, ge=0),
    _page: int = Query(1, ge=1),
):
    check_ups = await check_up_service.get_all_short_checkup(patient_id)
    check_ups = await area_service.get_all_areas()
    response.headers["X-Total-Count"] = str(len(check_ups))

    if _limit != 0:
        start = (_page - 1) * _limit
        end = start + _limit

        return check_ups[start:end]
    return check_ups

@router.get("/get_check_up/{check_up_id}")
async def get_check_up(
    check_up_id: int,
    check_up_service: Annotated[CheckUpService, Depends(check_up_service)],
):
    check_ups = await check_up_service.get_check_up(check_up_id)
    return check_ups


@router.post("/add_new")
async def add_new_check_up(
    data: CheckUpSchemaAdd,
    check_up_service: Annotated[CheckUpService, Depends(check_up_service)],
):
    check_up_id = await check_up_service.add_new_check_up(data)
    return check_up_id

