from utils.repository import AbstractRepository


class CheckUpService:
    def __init__(self, check_up_repo: AbstractRepository):
        self.check_up_repo: AbstractRepository = check_up_repo()
    
    async def get_all_short_checkup(self, id):
        all_short_checkup = await self.check_up_repo.get_all_short_checkup(id)
        return all_short_checkup
    
    async def get_check_up(self, id):
        get_check_up = await self.check_up_repo.get_check_up(id)
        return get_check_up
    
    async def get_all_check_up_places(self):
        check_up_places = await self.check_up_repo.find_all()
        return check_up_places
    




