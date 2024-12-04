from utils.repository import AbstractRepository

from models import Area

class AreaService:
    def __init__(self, area_repo: AbstractRepository):
        self.area_repo: AbstractRepository = area_repo()

    async def get_all_areas(self):
        all_areas = await self.area_repo.find_all()
        return all_areas

    async def add_new_area(self, area):
        newArea = Area(id=area.id)
        if added_area := await self.area_repo.add_one(newArea):
            return added_area
        raise HTTPException(
                status_code=400,
                detail="Insert error"
            )