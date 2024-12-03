from utils.repository import AbstractRepository
from fastapi import HTTPException 

from models import AddressArea

class AddressService:
    def __init__(self, address_repo: AbstractRepository):
        self.address_repo: AbstractRepository = address_repo()
    
    async def get_address_id(self, address_data):
        address_info = AddressArea(street=data.street, house=data.house, 
            building=data.building, flat=data.flat)
        if address_id := await self.address_repo.find_address(address_info):
            return address_id
        return None