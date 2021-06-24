"""Async client module"""

from typing import Any

import httpx
from fastapi import status

from app.core.config import settings

client = httpx.AsyncClient()


async def fetch(param: str) -> Any:
    """"""
    # gets pokemon details from pokemon endpoint
    POKEMON_BASE_API = settings.Config.POKEMON_BASE_API
    POKEMON_URL = f"{POKEMON_BASE_API}/{param}"
    pokemon_api_res = await client.get(POKEMON_URL)

    if pokemon_api_res.status_code == 404:
        response = {
            "status": False,
            "status_code": status.HTTP_404_NOT_FOUND,
            "message": "Given Pokémon name is not found!",
        }
        return response

    pokemon_json = pokemon_api_res.json()

    # gets pokemon's species details from the species
    # url extracted from previous call
    POKEMON_SPECIES_URL = pokemon_json["species"]["url"]
    species_api_res = await client.get(POKEMON_SPECIES_URL)
    species_json = species_api_res.json()

    response = {
        "status": True,
        "status_code": status.HTTP_200_OK,
        "message": species_json,
    }
    return response
