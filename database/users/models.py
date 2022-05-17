from tortoise.exceptions import ValidationError
from fastapi_users_db_tortoise import TortoiseBaseUserModel
from tortoise import fields

import settings


def check_username_not_empty(value: str):
    if not value.strip():
        raise ValidationError("Empty username is not allowed")
    return value


class UserModel(TortoiseBaseUserModel):
    username = fields.CharField(
        null=False,
        max_length=settings.MAX_USERNAME_LENGTH,
        validators=[
            check_username_not_empty,
        ],
    )


def get_user_model():
    return UserModel
