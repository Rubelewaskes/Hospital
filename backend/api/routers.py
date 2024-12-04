from api.address import router as router_address
from api.area import router as router_area
from api.check_up import router as router_check_up
from api.diagnosis import router as router_diagnosis
from api.doctor import router as router_doctor
from api.gender import router as router_gender
from api.patient import router as router_patient
from api.symptom import router as router_symptom

all_routers = [
    router_address, router_area,
    router_check_up, router_diagnosis,
    router_doctor, router_gender, 
    router_patient, router_symptom,
]