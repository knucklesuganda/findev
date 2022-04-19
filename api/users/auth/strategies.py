from fastapi_users.authentication import JWTStrategy

import settings


def get_strategy():
    return JWTStrategy(secret=settings.USER_AUTH_SECRET, lifetime_seconds=settings.USER_AUTH_MAX_AGE)
