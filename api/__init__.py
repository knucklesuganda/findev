from hypercorn import Config
from hypercorn.asyncio import serve

from api.api import app


async def run_api():
    await serve(get_app(), Config())


def get_app():
    return app
