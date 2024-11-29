from fastapi import (
    APIRouter,
    Depends,
    Form,
    HTTPException,
    status,
)
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from auth import utils
from pydantic import BaseModel

http_bearer = HTTPBearer()

class TokenInfo(BaseModel):
    access_token: str
    token_type: str

class UserSchema(BaseModel):
    id: str 
    username: str
    password: str
    email: str | None
    is_doctor: bool
    active: bool = True

router = APIRouter(prefix="/jwt", tags=["JWT"])

ivan = UserSchema (
    id = "1",
    username="ivan",
    password="12345",
    email = "doctor@mail.ru",
    is_doctor = True,
    active = True
)
peter = UserSchema (
    id = "2",
    username="peter",
    password="123",
    email=None,
    is_doctor = False,
    active = True
)

users_db: dict[str, UserSchema] = {
    ivan.username: ivan,
    peter.username: peter
}

def validate_auth_user(
    username: str = Form(),
    password: str = Form()
):
    unauthed_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="invalid username or password"
    )
    if not (user := users_db.get(username)):
        raise unauthed_exc
    if user.password != password:
        raise unauthed_exc
    return user



@router.post("/login", response_model=TokenInfo)
def auth_user_issue_jwt(
    user: UserSchema = Depends(validate_auth_user)
):
    jwt_payload = {
        "sub": user.username,
        "username": user.username,
        "email": user.email
    }
    token = utils.encode_jwt(jwt_payload)
    return TokenInfo(
        access_token=token,
        token_type="Bearer"
    )


def get_current_auth_user(
    credentials: HTTPAuthorizationCredentials = Depends(http_bearer)
) -> UserSchema:
    token = credentials.credentials
    payload = utils.decode_jwt(
        token=token
    )
    username: str = payload.get("sub")
    print(username)
    if user := users_db.get(username):
        return user
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="token invalid"
    )

def get_current_active_auth_user(
    user: UserSchema = Depends(get_current_auth_user)
):
    if user.active:
        return user
    else:
        raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="user inactive"
    )

@router.get("/users/me/")
def auth_user_check_self_info(
    user: UserSchema = Depends(get_current_active_auth_user)
):
    return {
        "username": user.username,
        "email": user.email
    }