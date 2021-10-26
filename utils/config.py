
from environs import Env

env = Env()
env.read_env()

USERNAME = env.str("INSTAGRAM_USERNAME")
PASSWORD = env.str("PASSWORD")
PROFILE_LINK = env.str("PROFILE_LINK")
