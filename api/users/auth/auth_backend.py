from typing import Sequence

from fastapi_users.authentication import AuthenticationBackend

from .transports import get_transport
from .strategies import get_strategy


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=get_transport(),
    get_strategy=get_strategy,
)


def get_auth_backends() -> Sequence[AuthenticationBackend]:
    return [auth_backend]
