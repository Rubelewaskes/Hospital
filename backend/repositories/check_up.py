from models.check_up import CheckUp
from utils.repository import SQLAlchemyRepositoryCheckUp


class CheckUpRepository(SQLAlchemyRepositoryCheckUp):
    model = CheckUp