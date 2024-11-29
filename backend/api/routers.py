from api.patient import router as router_patient
from api.check_up import router as router_check_up
from api.gender import router as router_gender

all_routers = [
    router_patient,
    router_check_up,
    router_gender
]