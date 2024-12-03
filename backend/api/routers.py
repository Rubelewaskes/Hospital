from api.patient import router as router_patient
from api.check_up import router as router_check_up
from api.gender import router as router_gender
from api.diagnosis import router as router_diagnosis
from api.symptom import router as router_symptom

all_routers = [
    router_patient,
    router_check_up,
    router_gender,
    router_diagnosis,
    router_symptom,
]