from models.patient import Patient
from utils.repository import SQLAlchemyRepository


class PatientRepository(SQLAlchemyRepository):
    model = Patient