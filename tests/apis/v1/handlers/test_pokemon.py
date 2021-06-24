"""Test pokemon module"""

from fastapi.testclient import TestClient

from app.core import settings


def test_get_pokemon(client: TestClient) -> None:
    response = client.get(f"{settings.API_V1_STR}/pokemon/mewtwo")
    pokemon = response.json()
    assert response.status_code == 200
    assert pokemon["name"] == "mewtwo"


def test_pokemon_not_found(client: TestClient) -> None:
    response = client.get(f"{settings.API_V1_STR}/pokemon/asd")
    pokemon = response.json()

    assert response.status_code == 404
    assert pokemon["status"] is False


def test_pokemon_wrong_endpoint(client: TestClient) -> None:
    response = client.get(f"{settings.API_V1_STR}/pokemon/")
    assert response.status_code == 404
