from typing import Annotated
from fastapi import APIRouter, Depends

from api.dependencies import check_up_place_service
from services.check_up_place import CheckUpPlaceService


router = APIRouter(
    prefix="/check_up",
    tags=["Check_up"],
)

@router.get("/get_all_places")
async def get_all_check_up_places(
    check_up_place_service: Annotated[CheckUpPlaceService, Depends(check_up_place_service)],
):
    check_up_places = await check_up_place_service.get_all_check_up_places()

    return check_up_places