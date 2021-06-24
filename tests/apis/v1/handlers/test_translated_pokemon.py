"""Test translated pokemon module"""

from fastapi.testclient import TestClient

from app.core import settings


def test_get_translated_pokemon(client: TestClient) -> None:
    response = client.get(f"{settings.API_V1_STR}/pokemon/translated/mewtwo")
    pokemon = response.json()
    assert response.status_code == 200
    assert pokemon["name"] == "mewtwo"


def test_pokemon_not_found(client: TestClient) -> None:
    response = client.get(f"{settings.API_V1_STR}/pokemon/translated/asd")
    pokemon = response.json()

    assert response.status_code == 404
    assert pokemon["status"] is False


def test_pokemon_wrong_endpoint(client: TestClient) -> None:
    response = client.get(f"{settings.API_V1_STR}/pokemon/translated")
    assert response.status_code == 404
