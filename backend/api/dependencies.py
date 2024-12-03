from repositories.patient import PatientRepository
from repositories.address import AddressAreaRepository
from repositories.check_up import CheckUpRepository, CheckUpPlaceRepository, SymptomRepository
from repositories.gender import GenderRepository
from repositories.diagnosis import DiagnosisRepository
from services import (
    PatientService, CheckUpService,
    SymptomService, GenderService,
    CheckUpPlaceService, DiagnosisService, 
    AddressService
)

def address_service():
    return AddressService(AddressAreaRepository)

def patient_service():
    return PatientService(PatientRepository)

def check_up_service():
    return CheckUpService(CheckUpRepository)

def symptom_service():
    return SymptomService(SymptomRepository)

def diagnosis_service():
    return DiagnosisService(DiagnosisRepository)

def check_up_place_service():
    return CheckUpPlaceService(CheckUpPlaceRepository)

def gender_service():
    return GenderService(GenderRepository)
