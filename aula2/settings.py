# settings.py
import os
from dotenv import load_dotenv
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
DATABASE_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DATABASE_USER = os.getenv("POSTGRES_USER")
