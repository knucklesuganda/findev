from tortoise.contrib.fastapi import register_tortoise

import settings
from api import get_app


def create_database_connection():
    register_tortoise(get_app(), config=settings.DATABASE_CONFIG)
