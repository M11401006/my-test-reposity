import os
from dotenv import load_dotenv
load_dotenv()

api_KEY = os.getenv("API_KEY")
database_URL = os.getenv("DATABASE_URL")
secret_KEY = os.getenv("SECRET_KEY")

print(api_KEY)
print(database_URL)
print(secret_KEY)