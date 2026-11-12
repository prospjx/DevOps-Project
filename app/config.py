import os

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "Task Management API"
    APP_VERSION: str = "1.0.0"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True
    DATABASE_URL: str = "sqlite:///./tasks.db"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()

if os.getenv("VERCEL") and not os.getenv("DATABASE_URL"):
    settings.DATABASE_URL = "sqlite:////tmp/tasks.db"
