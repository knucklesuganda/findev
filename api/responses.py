import typing

from fastapi.responses import JSONResponse

import settings


class CustomJSONResponse(JSONResponse):
    def render(self, content: typing.Any) -> bytes:
        if isinstance(content, dict):
            content['version'] = settings.API_VERSION

        return super(CustomJSONResponse, self).render(content)
