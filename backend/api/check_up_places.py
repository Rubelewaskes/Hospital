from typing import Annotated
from fastapi import APIRouter, Depends

from api.dependencies import check_up_place_service
from services.check_up_place import CheckUpPlaceService

from auth.users import  current_active_user
from auth.db import User


router = APIRouter(
    prefix="/check_up",
    tags=["Check_up"],
)

@router.get("/get_all_places")
async def get_all_check_up_places(
    check_up_place_service: Annotated[CheckUpPlaceService, Depends(check_up_place_service)],
    user: User = Depends(current_active_user),
):
    if user.is_doctor or user.is_superuser:
        check_up_places = await check_up_place_service.get_all_check_up_places()
        return check_up_places
    
    raise HTTPException(
            status_code=403,
            detail="Forbidden"
        )
    


   