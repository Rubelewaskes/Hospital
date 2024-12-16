from fastapi import APIRouter

from api.address import router as router_address
from api.area import router as router_area
from api.check_up import router as router_check_up
from api.check_up_places import router as router_check_up_places
from api.diagnosis import router as router_diagnosis
from api.doctor import router as router_doctor
from api.gender import router as router_gender
from api.patient import router as router_patient
from api.symptom import router as router_symptom
from auth.routes import router as router_auth

from auth.users import auth_backend, fastapi_users
from auth.schemas import UserCreate, UserRead, UserUpdate

router_cookie_auth = fastapi_users.get_auth_router(auth_backend)
router_register = fastapi_users.get_register_router(UserRead, UserCreate)
router_users_auth = fastapi_users.get_users_router(UserRead, UserUpdate)

router_cookie_auth.prefix = "/auth/cookie"
router_cookie_auth.tags = ["Auth"]

router_register.prefix = "/auth"
router_register.tags = ["Auth"]

router_users_auth.prefix = "/auth"
router_users_auth.tags = ["Auth"]

all_routers = [
    router_address, 
    router_area,
    router_check_up, 
    router_check_up_places,
    router_diagnosis,
    router_doctor, 
    router_gender, 
    router_patient, 
    router_symptom,
    router_cookie_auth,
    router_register,
    router_users_auth,
    router_auth
]