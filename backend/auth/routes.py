from fastapi import Depends, FastAPI, APIRouter

from auth.db import User, create_db_and_tables
from auth.users import  current_active_user, fastapi_users

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

@router.get("/authenticated-route")
async def authenticated_route(user: User = Depends(current_active_user)):
    return {"message": f"Hello {user.email}!"}

@router.get("/get_role")
async def get_user_role(user: User = Depends(current_active_user)):
    if user.is_superuser:
        return {"message": f"Hello Admin {user.email}!"}
    if user.is_doctor:
        return {"message": f"Hello Doctor {user.email}!"}
    else:
        return {"message": f"Hello Patient {user.email}!"}