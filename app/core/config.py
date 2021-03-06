"""Application settings and configurations"""

import os

from dotenv import load_dotenv
from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Pokedex API service"

    class Config:
        load_dotenv("./.env")
        PORT = os.getenv("PORT")
        POKEMON_BASE_API = os.getenv("POKEMON_BASE_API")
        SHAKESPEARE_TRANSLATION_API = os.getenv("SHAKESPEARE_TRANSLATION_API")
        YODA_TRANSLATION_API = os.getenv("YODA_TRANSLATION_API")


settings = Settings()
