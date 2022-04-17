from fastapi_users import BaseUserManager

import settings
from .schemas import UserCreate, UserDB


class UserManager(BaseUserManager[UserCreate, UserDB]):
    user_db_model = UserDB
    reset_password_token_secret = settings.USER_RESET_PASSWORD_TOKEN_SECRET
    verification_token_secret = settings.USER_VERIFICATION_TOKEN_SECRET


def create_user_manager():
    return UserManager
