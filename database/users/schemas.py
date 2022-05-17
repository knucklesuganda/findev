from typing import Optional

from fastapi_users import models
from fastapi_users.models import BaseUserDB
from tortoise.contrib.pydantic import PydanticModel
from pydantic import ConstrainedStr

import settings
from database.users.models import get_user_model


class UsernameField(ConstrainedStr):
    min_length = settings.MIN_USERNAME_LENGTH
    max_length = settings.MAX_USERNAME_LENGTH
    strip_whitespace = True


class User(models.BaseUser):
    username: UsernameField


class UserCreate(models.BaseUserCreate):
    username: UsernameField


class UserUpdate(models.BaseUserUpdate):
    username: Optional[UsernameField]


class UserDB(User, BaseUserDB, PydanticModel):
    class Config:
        orm_mode = True
        orig_model = get_user_model()


def get_user_schema():
    return UserDB
