from typing import Annotated
from fastapi import APIRouter, Depends, Query, Response

from api.dependencies import address_service
from services import AddressService
from schemas import AddressAreaSchema, AddressAreaSchemaAdd

from auth.users import  current_active_user
from auth.db import User

router = APIRouter(
    prefix="/address",
    tags=["Address"],
)

@router.get("/get_all")
async def get_all_addresses(
    address_service: Annotated[AddressService, Depends(address_service)],
    response: Response,
    _limit: int = Query(0, ge=0),
    _page: int = Query(1, ge=1),
    user: User = Depends(current_active_user),
):
    if user.is_superuser:
        addresses = await address_service.get_all_addresses()
        response.headers["X-Total-Count"] = str(len(addresses))

        if _limit != 0:
            start = (_page - 1) * _limit
            end = start + _limit

            return addresses[start:end]
        return addresses

    raise HTTPException(
            status_code=403,
            detail="Forbidden"
        )

@router.put("/update_one")
async def update_one_address(
    upd_address: AddressAreaSchema,
    address_service: Annotated[AddressService, Depends(address_service)],
    user: User = Depends(current_active_user),
):
    if user.is_superuser:
        address = await address_service.update_address(upd_address)
        return address
        
    raise HTTPException(
            status_code=403,
            detail="Forbidden"
        )

@router.post("/add_new")
async def add_address(
    new_address: AddressAreaSchemaAdd,
    address_service: Annotated[AddressService, Depends(address_service)],
    user: User = Depends(current_active_user),
):
    if user.is_superuser:
        address = await address_service.add_new_address(new_address)
        return address

    raise HTTPException(
            status_code=403,
            detail="Forbidden"
        )