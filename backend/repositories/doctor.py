from models import Doctor
from utils import SQLAlchemyRepositoryDoctor

class DoctorRepository(SQLAlchemyRepositoryDoctor):
    model = Doctor