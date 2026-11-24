import tomllib
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

PROJECT_ROOT = Path(__file__).resolve().parents[2]

with open(PROJECT_ROOT / "pyproject.toml", "rb") as file:
    project_config = tomllib.load(file)


class Settings(BaseSettings):
    # Default values: used when the variables are not defined in .env or system environment.
    APP_NAME: str = "Clinova"
    APP_PORT: int = 7070
    APP_VERSION: str = project_config["project"]["version"]
    DEBUG: bool = True

    # Database configuration
    DATABASE_URL: str

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
