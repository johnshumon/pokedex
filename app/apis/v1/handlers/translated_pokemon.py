"""Translated pokemon module"""

from typing import Any

from fastapi import APIRouter

from app.core.config import settings
from app.utils.async_client import client
from app.utils.translate import shakespeare_translation

router = APIRouter()


@router.get("")
async def get_translated_pokemon(pokemon_name: str) -> Any:
    """Handler for getting a translated pokemon"""

    # gets pokemon details from pokemon endpoint
    POKEMON_BASE_API = settings.Config.POKEMON_BASE_API
    POKEMON_URL = f"{POKEMON_BASE_API}/{pokemon_name}"
    pokemon_api_res = await client.get(POKEMON_URL)
    pokemon_json = pokemon_api_res.json()

    # gets pokemon's species details from the species
    # url extracted from previous call
    POKEMON_SPECIES_URL = pokemon_json["species"]["url"]
    species_api_res = await client.get(POKEMON_SPECIES_URL)
    species_json = species_api_res.json()

    # set values for result
    name = pokemon_json["name"]
    habitat = species_json["habitat"]["name"]
    is_legendary = species_json["is_legendary"]

    if habitat == "cave":
        print("Yoda")
        description = species_json["flavor_text_entries"][0]["flavor_text"]
    else:
        description = species_json["flavor_text_entries"][0]["flavor_text"]
        # description = None
        translated_desc = await shakespeare_translation(description)

    result = {
        "name": name,
        "description": translated_desc,
        "habitat": habitat,
        "isLegendary": is_legendary,
    }

    return result
