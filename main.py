import asyncio

from api import run_api
from database.database_connection import connect_database


async def main():
    connect_database()
    await run_api()


if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(main())
