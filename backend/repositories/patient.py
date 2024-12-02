from models.patient import Patient
from models.area import AddressArea
from utils.repository import SQLAlchemyRepositoryPatient


class PatientRepository(SQLAlchemyRepositoryPatient):
    model = Patient

class PatientAddressAreaRepository(SQLAlchemyRepositoryPatient):
    model = AddressArea