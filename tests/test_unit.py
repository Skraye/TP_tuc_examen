from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_trainer():
    """
        Recuperation de la liste des Trainers
    """
    response = client.get("trainers/1")
    assert response.status_code == 200
    assert response.json() == {"name": "Mahat", "birthdate": "2022-11-07", "id":1, "inventory": [], "pokemons": []}

def test_pokemons_random():
    """
        Recuperation de 3 pokemons aleatoires
    """
    response = client.get("/pokemons/random/")
    assert response.status_code == 200
    assert len(response.json()) == 3

def test_pokemons_random_different():
    """
        Recuperation de 3 pokemons aleatoires different
    """
    response = client.get("/pokemons/random/")
    assert response.status_code == 200
    assert response.json()[0]["id"] != response.json()[1]["id"] != response.json()[2]["id"]

def test_get_items():
    """
        Recuperation de la liste des items
    """
    response = client.get("/items")
    assert response.status_code == 200
    assert response.json()[0] == {"name": "MahatBall", "description": "Trop issou", "id": 1, "trainer_id": 2}

def test_get_pokemons():
    """
        Recuperation de la liste des pokemons
    """
    response = client.get("/pokemons")
    assert response.status_code == 200
    assert response.json()[0] == {"api_id": 2, "custom_name": "Bulbi", "id": 1, "name": "ivysaur", "trainer_id": 2}

def test_pokemon_battle():
    """
        Test de la fonction de combat
    """
    response = client.get("/pokemons/battle/2/6")
    assert response.status_code == 200
    assert response.json() == {"pokemonApiID": 6, "result": -129}

def test_pokemon_battle_draw():
    """
        Test de la fonction de combat si egalite
    """
    response = client.get("/pokemons/battle/2/2")
    assert response.status_code == 200
    assert response.json() == {"pokemonApiID": None, "result": 0}
