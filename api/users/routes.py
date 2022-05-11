from fastapi import Depends
from fastapi_users import FastAPIUsers

from api.users.auth.auth_backend import get_auth_backends
from database.users.adapters import get_user_adapter
from database.users.managers import create_user_manager
from database.users.schemas import User, UserCreate, UserUpdate, UserDB

UserManager = create_user_manager()


async def get_user_manager(user_db=Depends(get_user_adapter)):
    yield UserManager(user_db)


fastapi_users = FastAPIUsers(
    get_user_manager,
    get_auth_backends(),
    User,
    UserCreate,
    UserUpdate,
    UserDB,
)


def get_auth_routers():
    routers = []

    for auth_backend in get_auth_backends():
        routers.append({
            "prefix": f"/users/{auth_backend.name}",
            "router": fastapi_users.get_auth_router(auth_backend),
        })

    return routers


def get_register_router():
    return fastapi_users.get_register_router()
