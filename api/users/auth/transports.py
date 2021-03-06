from fastapi_users.authentication import CookieTransport

import settings


def get_transport():
    return CookieTransport(
        cookie_name='user_auth',
        cookie_max_age=settings.USER_AUTH_MAX_AGE,
    )
