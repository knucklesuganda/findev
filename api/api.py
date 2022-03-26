from fastapi import FastAPI

from api.responses import CustomJSONResponse


app = FastAPI(
    default_response_class=CustomJSONResponse,
)


@app.get('/')
async def test_route():
    return {
        "hello": False,
    }


@app.get('/2')
async def test_route2():
    return {
        "second_route": False,
    }

