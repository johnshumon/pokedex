"""Pokemon module"""

from typing import Any

from fastapi import APIRouter, Response, status

from app.core.config import settings
from app.utils.async_client import client

router = APIRouter()


@router.get("")
async def get_pokemon(pokemon_name: str, response: Response) -> Any:
    """Handler for getting details of a pokemon"""

    # gets pokemon details from pokemon endpoint
    POKEMON_BASE_API = settings.Config.POKEMON_BASE_API
    POKEMON_URL = f"{POKEMON_BASE_API}/{pokemon_name}"
    pokemon_api_res = await client.get(POKEMON_URL)

    if pokemon_api_res.status_code == 404:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": "Not found"}

    pokemon_json = pokemon_api_res.json()

    # gets pokemon's species details from the species
    # url extracted from previous call
    POKEMON_SPECIES_URL = pokemon_json["species"]["url"]
    species_api_res = await client.get(POKEMON_SPECIES_URL)
    species_json = species_api_res.json()

    # set values for result
    name = pokemon_json["name"]
    description = species_json["flavor_text_entries"][0]["flavor_text"]
    habitat = species_json["habitat"]["name"]
    is_legendary = species_json["is_legendary"]

    result = {
        "name": name,
        "description": description,
        "habitat": habitat,
        "isLegendary": is_legendary,
    }

    return result
