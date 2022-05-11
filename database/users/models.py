from fastapi_users_db_tortoise import TortoiseBaseUserModel
from tortoise import fields

import settings


class UserModel(TortoiseBaseUserModel):
    # TODO: check username not empty
    username = fields.CharField(null=False, max_length=settings.MAX_USERNAME_LENGTH)


def get_user_model():
    return UserModel
