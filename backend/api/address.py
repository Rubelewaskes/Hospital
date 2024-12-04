from typing import Annotated
from fastapi import APIRouter, Depends

from api.dependencies import address_service
from services import AddressService
from schemas import AddressAreaSchemaAdd

router = APIRouter(
    prefix="/address",
    tags=["Address"],
)

@router.post("/add_new")
async def add_address(
    new_address: AddressAreaSchemaAdd,
    address_service: Annotated[AddressService, Depends(address_service)],
):
    address = await address_service.add_new_address(new_address)
    return address
