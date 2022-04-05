from fastapi_users_db_tortoise import TortoiseUserDatabase

from database.users.models import get_user_model
from database.users.schemas import get_user_schema


async def get_user_adapter():
    yield TortoiseUserDatabase(get_user_schema(), get_user_model())
