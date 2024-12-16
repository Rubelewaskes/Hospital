from typing import Annotated
from fastapi import APIRouter, Depends, Query, Response

from api.dependencies import area_service
from services import AreaService
from schemas import AreaSchema

from auth.users import  current_active_user
from auth.db import User

router = APIRouter(
    prefix="/area",
    tags=["Area"],
)

@router.get("/get_areas")
async def get_all_areas(
    area_service: Annotated[AreaService, Depends(area_service)],
    response: Response,
    _limit: int = Query(0, ge=0),
    _page: int = Query(1, ge=1),
    user: User = Depends(current_active_user),
):
    if user.is_superuser:
        areas = await area_service.get_all_areas()
        response.headers["X-Total-Count"] = str(len(areas))

        if _limit != 0:
            start = (_page - 1) * _limit
            end = start + _limit

            return areas[start:end]
        return areas
    raise HTTPException(
            status_code=403,
            detail="Forbidden"
        )

@router.post("/add_new")
async def add_area(
    new_area: AreaSchema,
    area_service: Annotated[AreaService, Depends(area_service)],
    user: User = Depends(current_active_user),
):
    if user.is_superuser:
        area = await area_service.add_new_area(new_area)
        return area

    raise HTTPException(
            status_code=403,
            detail="Forbidden"
        )