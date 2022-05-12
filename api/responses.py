import typing

from fastapi.responses import JSONResponse

import settings


class CustomJSONResponse(JSONResponse):
    def render(self, content: typing.Any) -> bytes:
        return super(CustomJSONResponse, self).render({
            "data": content,
            "version": settings.API_VERSION,
        })
