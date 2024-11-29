from models.check_up import CheckUp, CheckUpPlace, Symptom
from utils.repository import SQLAlchemyRepositoryCheckUp, SQLAlchemyRepository


class CheckUpRepository(SQLAlchemyRepositoryCheckUp):
    model = CheckUp

class CheckUpPlaceRepository(SQLAlchemyRepository):
    model = CheckUpPlace

class SymptomRepository(SQLAlchemyRepository):
    model = Symptom