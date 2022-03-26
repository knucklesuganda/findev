from fastapi import FastAPI

from api.responses import CustomJSONResponse


app = FastAPI(default_response_class=CustomJSONResponse)


@app.get('/')
async def test_view():
    return {
        "ok": True,
    }


@app.get('/second')
async def second_view():
    return {
        "second_ok": True,
    }
