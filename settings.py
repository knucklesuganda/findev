import environs

env = environs.Env()
env.read_env('.env')

API_VERSION = env('API_VERSION')
