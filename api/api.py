from fastapi import FastAPI

from api.responses import CustomJSONResponse
from api.users.routes import get_auth_routers, get_register_router, get_users_router


app = FastAPI(default_response_class=CustomJSONResponse)

for router in get_auth_routers():
    app.include_router(router['router'], prefix=router['prefix'])


app.include_router(router=get_register_router(), prefix='/users')
app.include_router(router=get_users_router(), prefix='/users')
