from fastapi import FastAPI

from api.responses import CustomJSONResponse
from api.users.routes import get_auth_routers, get_register_router

app = FastAPI(default_response_class=CustomJSONResponse)
# TODO: rename username field in login to email

for router in get_auth_routers():
    app.include_router(router['router'], prefix=router['prefix'])

app.include_router(router=get_register_router(), prefix='/users')
