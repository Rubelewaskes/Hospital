from models import CheckUp, CheckUpPlace, Symptom
from utils import SQLAlchemyRepositoryCheckUp, SQLAlchemyRepository


class CheckUpRepository(SQLAlchemyRepositoryCheckUp):
    model = CheckUp

class CheckUpPlaceRepository(SQLAlchemyRepository):
    model = CheckUpPlace

