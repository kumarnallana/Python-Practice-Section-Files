import os
from pathlib import Path

from dotenv import load_dotenv


env_path = Path(__file__).parent / ".env"

load_dotenv(env_path)

app_name = os.getenv("APP_NAME")
app_env = os.getenv("APP_ENV")
debug = os.getenv("DEBUG")

print(app_name)
print(app_env)
print(debug)
