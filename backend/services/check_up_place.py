from utils.repository import AbstractRepository


class CheckUpPlaceService:
    def __init__(self, check_up_repo: AbstractRepository):
        self.check_up_repo: AbstractRepository = check_up_repo()
    
    async def get_all_check_up_places(self):
        check_up_places = await self.check_up_repo.find_all()
        return check_up_places