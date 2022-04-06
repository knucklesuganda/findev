from fastapi_users_db_tortoise import TortoiseBaseUserModel


class UserModel(TortoiseBaseUserModel):
    pass


def get_user_model():
    return UserModel
