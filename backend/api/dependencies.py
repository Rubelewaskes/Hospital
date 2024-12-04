from repositories import (
    AddressAreaRepository, AreaRepository,
    CheckUpRepository, CheckUpPlaceRepository,
    DiagnosisRepository, DoctorRepository, 
    GenderRepository, PatientRepository, 
    SymptomRepository,
)
from services import (
    AddressService, AreaService,
    CheckUpService, CheckUpPlaceService,
    DiagnosisService, DoctorService, 
    GenderService, PatientService, 
    SymptomService,
)

def address_service():
    return AddressService(AddressAreaRepository)

def area_service():
    return AreaService(AreaRepository)

def check_up_service():
    return CheckUpService(CheckUpRepository)

def check_up_place_service():
    return CheckUpPlaceService(CheckUpPlaceRepository)
    
def diagnosis_service():
    return DiagnosisService(DiagnosisRepository)

def doctor_service():
    return DoctorService(DoctorRepository)

def gender_service():
    return GenderService(GenderRepository)

def patient_service():
    return PatientService(PatientRepository)

def symptom_service():
    return SymptomService(SymptomRepository)





