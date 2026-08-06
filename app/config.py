from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Task API"
    APP_VERSION: str = "1.0.0"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True
    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/postgres"

    class Config:
        env_file = ("app/.env", ".env")


settings = Settings()
