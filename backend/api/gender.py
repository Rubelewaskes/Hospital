from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException 

from api.dependencies import gender_service
from services.gender import GenderService

router = APIRouter(
    prefix="/gender",
    tags=["Gender"],
)

@router.get("/get_all")
async def get_all_genders(
    gender_service: Annotated[GenderService, Depends(gender_service)],
):
    genders = await gender_service.get_all_genders()
    return genders