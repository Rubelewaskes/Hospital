from repositories.patient import PatientRepository
from services.patient import PatientService
from repositories.check_up import CheckUpRepository
from services.check_up import CheckUpService



def patient_service():
    return PatientService(PatientRepository)

def check_up_service():
    return CheckUpService(CheckUpRepository)