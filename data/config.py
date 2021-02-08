from environs import Env

# Var to process .env-file
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")  # List of administrator user_ids
IP = env.str("ip")
