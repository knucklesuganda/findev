from fastapi_users.db import TortoiseUserDatabase

from .models import get_user_model
from .schemas import get_user_schema


async def get_user_adapter():
    yield TortoiseUserDatabase(get_user_schema(), get_user_model())
