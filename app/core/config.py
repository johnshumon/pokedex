"""Application core configuration"""

from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Pokedex API service"

    class Config:
        env_file = ".env"


settings = Settings()
