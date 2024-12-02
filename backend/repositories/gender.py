from models import Gender
from utils.repository import SQLAlchemyRepository


class GenderRepository(SQLAlchemyRepository):
    model = Gender