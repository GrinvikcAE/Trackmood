from fastapi_users.authentication import CookieTransport
from fastapi_users.authentication import AuthenticationBackend, BearerTransport, JWTStrategy
from config import SECRET_KEY

cookie_transport = CookieTransport(cookie_name='trackmood', cookie_max_age=86400)

SECRET = SECRET_KEY


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=86400)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)
