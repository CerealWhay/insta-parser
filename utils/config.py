
from environs import Env

env = Env()
env.read_env()

ACCOUNT_USERNAME = env.str("ACCOUNT_USERNAME")
ACCOUNT_PASSWORD = env.str("ACCOUNT_PASSWORD")
PROFILES = env.list("PROFILES")
