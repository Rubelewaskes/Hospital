from typing import Annotated
from fastapi import APIRouter, Depends

from api.dependencies import check_up_place_service
from services.check_up import CheckUpPlaceService


router = APIRouter(
    prefix="/check_up",
    tags=["Check_up"],
)

@router.get("/get_check_up_places")
async def get_check_up_places(
    check_up_place_service: Annotated[CheckUpPlaceService, Depends(check_up_place_service)],
):
    symptoms = await check_up_place_service.get_all_check_up_places()
    return symptoms