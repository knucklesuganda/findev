from fastapi import FastAPI

from api.responses import CustomJSONResponse
from api.users.api import get_auth_routers

app = FastAPI(default_response_class=CustomJSONResponse)


for auth_router in get_auth_routers():
    app.include_router(
        router=auth_router['router'],
        prefix=f'/{auth_router["name"]}',
    )
