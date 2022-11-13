"""Test pokemons functions
    """
from fastapi.testclient import TestClient
from main import app
from app.utils.pokeapi import get_pokemon_data, battle_pokemon
client = TestClient(app)

BASE_URL = "https://pokeapi.co/api/v2"


def test_get_pokemons():
    """Test /pokemons route
Sould return 200 status code
    """
    response = client.get("/pokemons")
    assert response.status_code == 200


def test_get_pokemon_id():
    """Test get_pokemon_data function
Should return the right pokemon name from api
    """
    api_id = 1
    response = get_pokemon_data(api_id)
    result = "bulbasaur"
    assert response["name"] == result


def test_battle_pokemon_vainqueur():
    """
        battle with pokemon_id_1 and pokemon_id_2
    """
    response = battle_pokemon(1, 2)
    result = "ivysaur"
    assert response == result
