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
    response: Response,
    _limit: int = Query(0, ge=0),
    _page: int = Query(1, ge=1),
):
    check_up_places = await check_up_place_service.get_all_check_up_places()
    check_up_places = await area_service.get_all_areas()
    response.headers["X-Total-Count"] = str(len(check_up_places))

    if _limit != 0:
        start = (_page - 1) * _limit
        end = start + _limit

        return check_up_places[start:end]
    return check_up_places