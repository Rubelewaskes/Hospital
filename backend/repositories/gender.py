from models import Gender
from utils import SQLAlchemyRepository


class GenderRepository(SQLAlchemyRepository):
    model = Gender