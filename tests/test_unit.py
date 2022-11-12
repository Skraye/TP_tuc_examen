"""
    UNIT TESTS
"""
from http import client
from fastapi.testclient import TestClient
from main import app
client = TestClient(app)

# Test 1
def test_get_trainer_by_name():
    """
        Check the get trainers by name endpoint
    """
    trainer_name = 'Alexis'
    response = client.get(f"/trainers/by_name/{trainer_name}")
    assert response.status_code == 200
    assert response.json()['id'] == 2

# Test 2
def test_get_trainers():
    """
        Check the get trainers endpoint
    """
    response = client.get("/trainers")
    assert response.status_code == 200
    assert len(response.json()) > 0

# Test 3
def test_get_items():
    """
        Check the get items endpoint
    """
    response = client.get("/items")
    assert response.status_code == 200
    assert len(response.json()) > 0

# Test 4
def test_get_pokemon():
    """
        Check the get pokemons endpoint
    """
    response = client.get("/pokemons")
    assert response.status_code == 200
    assert len(response.json()) > 0

# Test 5
def test_get_trainer():
    """
        Check the get trainer by id endpoint
    """
    response = client.get("trainers/2")
    assert response.status_code == 200
    assert response.json() == {"name": "Alexis", "birthdate": "2002-10-20",
        "id":2, "inventory": [], "pokemons": []}

# Test 6
def test_pokemons_random_different():
    """
        Check the get pokemon random endpoint : the 3 pokemons are different
    """
    response = client.get("/pokemons/random/")
    assert response.status_code == 200
    assert response.json()[0]["name"] != response.json()[1]["name"] != response.json()[2]["name"]

# Test 7
def test_3_pokemons_random():
    """
        Check the get pokemon random endpoint : it return exactly 3 pokemons
    """
    response = client.get("/pokemons/random/")
    assert response.status_code == 200
    assert len(response.json()) == 3
