from fastapi import FastAPI

from api.responses import CustomJSONResponse
from api.users.api import get_auth_routers, get_register_router

app = FastAPI(default_response_class=CustomJSONResponse)


for auth_router in get_auth_routers():
    app.include_router(
        router=auth_router['router'],
        prefix=f'/users/{auth_router["name"]}',
    )

app.include_router(get_register_router(), prefix="/users")
