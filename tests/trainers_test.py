import json
import pytest
from fastapi.testclient import TestClient
from main import app
from datetime import date

client = TestClient(app)

def test_trainer_lists(mocker):
    """
        validate if the trainers are returned
    """
    database_data = [
        {"name":"","birthdate":date(2000,1,24),"id":0,"inventory":[],"pokemons":[]},
        {"name":"","birthdate":date(2000,1,24),"id":1,"inventory":[],"pokemons":[]},
        {"name":"","birthdate":date(2000,1,24),"id":2,"inventory":[],"pokemons":[]},
        {"name":"","birthdate":date(2000,1,24),"id":3,"inventory":[],"pokemons":[]}
        ]
    response_data = [
        {"name":"","birthdate":"2000-01-24","id":0,"inventory":[],"pokemons":[]},
        {"name":"","birthdate":"2000-01-24","id":1,"inventory":[],"pokemons":[]},
        {"name":"","birthdate":"2000-01-24","id":2,"inventory":[],"pokemons":[]},
        {"name":"","birthdate":"2000-01-24","id":3,"inventory":[],"pokemons":[]}
        ]
    mocker.patch(
    "app.actions.get_trainers",
    return_value= database_data
    )
    response = client.get("trainers?skip=0&limit=100")
    assert response.status_code == 200
    assert response.json() == response_data
