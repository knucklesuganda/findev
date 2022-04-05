from fastapi_users import models
from fastapi_users.models import BaseUserDB
from pydantic import Field

import settings
from database.users.models import get_user_model


class User(models.BaseUser):
    username: str = Field(min_length=settings.MIN_USERNAME_LENGTH)


class UserCreate(models.BaseUserCreate):
    username: str = Field(min_length=settings.MIN_USERNAME_LENGTH)


class UserUpdate(models.BaseUserUpdate):
    username: str = Field(min_length=settings.MIN_USERNAME_LENGTH)


class UserDB(User, BaseUserDB):
    class Config:
        orm_mode = True
        orig_model = get_user_model()


def get_user_schema():
    return UserDB
