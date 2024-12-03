from models import Diagnosis
from utils import SQLAlchemyRepository


class DiagnosisRepository(SQLAlchemyRepository):
    model = Diagnosis