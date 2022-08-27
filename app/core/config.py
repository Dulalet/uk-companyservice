import pathlib

from pydantic import AnyHttpUrl, EmailStr, validator, BaseSettings
from typing import List, Optional, Union

# Project Directories
ROOT = pathlib.Path(__file__).resolve().parent.parent

PIECE = 796

SECRETS = {
    "SQL": "postgresql://daulet:qwerty@db/ukassa",
    "API_V1": "/api/v1"
}


class Settings(BaseSettings):
    API_V1_STR: str = SECRETS.get("API_V1")
    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    SQLALCHEMY_DATABASE_URI: Optional[str] = SECRETS.get("SQL")

    class Config:
        case_sensitive = True


settings = Settings()
