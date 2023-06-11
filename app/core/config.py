from pydantic import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()


class Settings(BaseSettings):
    database_url: str = os.getenv("FASTAPI_CRUD_APP_DATABASE_URL")

    class Config:
        env_file = ".env"


settings = Settings()
