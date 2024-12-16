from typing import Annotated
from fastapi import APIRouter, Depends, Query, Response

from api.dependencies import check_up_service
from services import CheckUpService
from schemas import CheckUpSchemaAdd

from auth.users import  current_active_user
from auth.db import User

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
    user: User = Depends(current_active_user),
):
    if user.is_doctor or user.is_superuser:
        check_ups = await check_up_service.get_all_short_checkup(patient_id)
        response.headers["X-Total-Count"] = str(len(check_ups))

        if _limit != 0:
            start = (_page - 1) * _limit
            end = start + _limit

            return check_ups[start:end]
        return check_ups
    
    raise HTTPException(
            status_code=403,
            detail="Forbidden"
        )

@router.get("/get_check_up/{check_up_id}")
async def get_check_up(
    check_up_id: int,
    check_up_service: Annotated[CheckUpService, Depends(check_up_service)],
    user: User = Depends(current_active_user),
):
    if user:
        check_ups = await check_up_service.get_check_up(check_up_id)
        return check_ups
    
    raise HTTPException(
            status_code=403,
            detail="Forbidden"
        )


@router.post("/add_new")
async def add_new_check_up(
    data: CheckUpSchemaAdd,
    check_up_service: Annotated[CheckUpService, Depends(check_up_service)],
    user: User = Depends(current_active_user),
):
    if user.is_superuser:
        check_up_id = await check_up_service.add_new_check_up(data)
        return check_up_id
    
    raise HTTPException(
            status_code=403,
            detail="Forbidden"
        )

