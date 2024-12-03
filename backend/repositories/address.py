from models import AddressArea
from utils import SQLAlchemyRepositoryPatient

class AddressAreaRepository(SQLAlchemyRepositoryPatient):
    model = AddressArea