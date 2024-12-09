import uuid

from fastapi_users import schemas


class UserRead(schemas.BaseUser[uuid.UUID]):
    is_doctor: bool


class UserCreate(schemas.BaseUserCreate):
    is_doctor: bool


class UserUpdate(schemas.BaseUserUpdate):
    is_doctor: bool