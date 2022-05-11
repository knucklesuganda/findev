from fastapi_users import models
from fastapi_users.models import BaseUserDB
from pydantic import Field
from tortoise.contrib.pydantic import PydanticModel

import settings
from database.users.models import get_user_model


def get_username_field():
    return Field(
        min_length=settings.MIN_USERNAME_LENGTH,
        max_length=settings.MAX_USERNAME_LENGTH,
    )


class User(models.BaseUser):
    username: str = get_username_field()


class UserCreate(models.BaseUserCreate):
    username: str = get_username_field()


class UserUpdate(models.BaseUserUpdate):
    username: str = get_username_field()


class UserDB(User, BaseUserDB, PydanticModel):
    class Config:
        orm_mode = True
        orig_model = get_user_model()


def get_user_schema():
    return UserDB
