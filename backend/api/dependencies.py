from repositories.patient import PatientRepository, PatientAddressAreaRepository
from services.patient import PatientService
from repositories.check_up import CheckUpRepository, CheckUpPlaceRepository, SymptomRepository
from services.check_up import CheckUpService
from repositories.gender import GenderRepository
from services.gender import GenderService


def patient_service():
    return PatientService(PatientRepository, PatientAddressAreaRepository)

def check_up_service():
    return CheckUpService(CheckUpRepository)

def symptom_service():
    return CheckUpService(SymptomRepository)

def check_up_place_service():
    return CheckUpService(CheckUpPlaceRepository)

def gender_service():
    return GenderService(GenderRepository)
