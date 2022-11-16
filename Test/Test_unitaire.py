from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

 #Recuperation de la liste des Trainers
def test_get_trainer():
   
    
    response = client.get("trainers/1")
    assert response.status_code == 200
    assert response.json() == {"name": "Med", "birthdate": "2022-11-12", "id":1, "inventory": [], "pokemons": []}

# Recuperation de 3 pokemons aleatoires
def test_pokemons_random():
   
    response = client.get("/pokemons/random/")
    assert response.status_code == 200
    assert len(response.json()) == 3

 #   Recuperation de 3 pokemons aleatoires different
def test_pokemons_random_different():
   
    response = client.get("/pokemons/random/")
    assert response.status_code == 200
    assert response.json()[0]["id"] != response.json()[1]["id"] != response.json()[2]["id"]

 # Recuperation de la liste des items
def test_get_items():
   
    response = client.get("/items")
    assert response.status_code == 200
    assert response.json()[0] == {"name": "Badr", "description": "Maroc", "id": 1, "trainer_id": 2}

# Recuperation de la liste des pokemons
def test_get_pokemons():
   
    response = client.get("/pokemons")
    assert response.status_code == 200
    assert response.json()[0] == {"api_id": 2, "custom_name": "tooto", "id": 1, "name": "blabla", "trainer_id": 2}

#Test Battle Function
def test_pokemon_battle():

    response = client.get("/pokemons/battle/2/6")
    assert response.status_code == 200
    assert response.json() == {"pokemonApiID": 6, "result": -129}

# Test if the batlle is Drawn
def test_pokemon_battle_draw():
    
    response = client.get("/pokemons/battle/2/2")
    assert response.status_code == 200
    assert response.json() == {"pokemonApiID": None, "result": 0}