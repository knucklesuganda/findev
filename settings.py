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
