from models import Patient
from models import AddressArea
from utils.repository import SQLAlchemyRepositoryPatient


class PatientRepository(SQLAlchemyRepositoryPatient):
    model = Patient

class PatientAddressAreaRepository(SQLAlchemyRepositoryPatient):
    model = AddressArea