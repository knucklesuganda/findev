from fastapi_users.authentication import AuthenticationBackend

from api.users.auth.strategies import get_strategy
from api.users.auth.transports import get_transport


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=get_transport(),
    get_strategy=get_strategy,
)


def get_auth_backends():
    return [
        auth_backend,
    ]

