from models import  Symptom
from utils import SQLAlchemyRepository

class SymptomRepository(SQLAlchemyRepository):
    model = Symptom