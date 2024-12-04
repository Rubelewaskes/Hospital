from typing import Annotated
from fastapi import APIRouter, Depends

from api.dependencies import area_service
from services import AreaService
from schemas import AreaSchema

router = APIRouter(
    prefix="/area",
    tags=["Area"],
)

@router.get("/get_areas")
async def get_all_areas(
    area_service: Annotated[AreaService, Depends(area_service)],
):
    areas = await area_service.get_all_areas()
    return areas

@router.post("/add_new")
async def add_area(
    new_area: AreaSchema,
    area_service: Annotated[AreaService, Depends(area_service)],
):
    area = await area_service.add_new_area(new_area)
    return area