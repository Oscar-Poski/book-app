# backend/app/core/config.py
from functools import lru_cache
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()  # carga .env si existe

class Settings(BaseModel):
    database_url: str

@lru_cache
def get_settings() -> Settings:
    return Settings(
        database_url=os.getenv("DATABASE_URL", "postgresql+psycopg2://postgres:postgres@localhost:5432/bookapp"),
    )
