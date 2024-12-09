from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException 

from api.dependencies import gender_service
from services.gender import GenderService

from auth.users import  current_active_user
from auth.db import User


router = APIRouter(
    prefix="/patient",
    tags=["Patient"],
)

@router.get("/get_all_genders")
async def get_two_genders(
    gender_service: Annotated[GenderService, Depends(gender_service)],
    user: User = Depends(current_active_user),
):
    if user:
        genders = await gender_service.get_all_genders()
        return genders
    raise HTTPException(
            status_code=403,
            detail="Forbidden"
        )