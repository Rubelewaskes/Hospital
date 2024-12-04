from models import Area
from utils import SQLAlchemyRepositoryPatient

class AreaRepository(SQLAlchemyRepositoryPatient):
    model = Area