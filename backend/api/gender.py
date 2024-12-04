from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException 

from api.dependencies import gender_service
from services.gender import GenderService

router = APIRouter(
    prefix="/patient",
    tags=["Patient"],
)

@router.get("/get_all_genders")
async def get_two_genders(
    gender_service: Annotated[GenderService, Depends(gender_service)],
):
    genders = await gender_service.get_all_genders()
    return genders