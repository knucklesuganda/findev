from fastapi import FastAPI

from api.responses import CustomJSONResponse
from api.users.routes import get_auth_routers

app = FastAPI(default_response_class=CustomJSONResponse)


for router in get_auth_routers():
    app.include_router(
        router['router'],
        prefix=router['prefix'],
        tags=["auth"],
    )

