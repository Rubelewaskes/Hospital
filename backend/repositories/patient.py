from models import Patient
from utils import SQLAlchemyRepositoryPatient


class PatientRepository(SQLAlchemyRepositoryPatient):
    model = Patient
