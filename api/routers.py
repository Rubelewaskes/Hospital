from api.patient import router as router_patient
from api.check_up import router as router_check_up

all_routers = [
    router_patient,
    router_check_up,
]