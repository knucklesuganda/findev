import environs

env = environs.Env()
env.read_env('.env')

API_VERSION = env('API_VERSION')


DATABASE_CONFIG = {
    "connections": {
        "default": env('DATABASE_CONNECTION_URL'),
    },
    "apps": {
        "models": {
            "models": [
                "aerich.models",
            ],
            "default_connection": "default",
        },
    },
}


MIN_USERNAME_LENGTH = env.int('MIN_USERNAME_LENGTH')
USER_AUTH_MAX_AGE = env.int('USER_AUTH_MAX_AGE')
USER_AUTH_SECRET = env('USER_AUTH_SECRET')
USER_RESET_PASSWORD_TOKEN_SECRET = env('USER_RESET_PASSWORD_TOKEN_SECRET')
USER_VERIFICATION_TOKEN_SECRET = env('USER_VERIFICATION_TOKEN_SECRET')
