import json
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_pokemons(mocker):
    """
        validate if the pokemons are returned
    """
    response_data = [
        {"api_id":5,"custom_name":"","id":0,"name":"","trainer_id":0},
        {"api_id":5,"custom_name":"","id":1,"name":"","trainer_id":0},
        {"api_id":5,"custom_name":"","id":2,"name":"","trainer_id":0},
        {"api_id":5,"custom_name":"","id":3,"name":"","trainer_id":0},
        ]
    mocker.patch(
    "app.actions.get_pokemons",
    return_value= response_data
    )
    response = client.get("pokemons/?skip=0&limit=100")
    assert response.status_code == 200
    assert response.json() == response_data
