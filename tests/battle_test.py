import json
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)



def test_battle_draw():
    """
    Validation of battle in case of draw
    """
    # Arrange
    post_data = {
            "pokemon_right": {
                "api_id": 5,
                "custom_name": "string",
                "id": 1,
                "name": "string",
                "trainer_id": 0
            },
            "pokemon_left": {
                "api_id": 5,
                "custom_name": "string",
                "id": 2,
                "name": "string",
                "trainer_id": 0
            }
        }
    response_data = {"winner": "draw"}
    # Act
    response = client.post(
        "/battle/1/2",
        headers={'accept': 'application/json', 'Content-Type': 'application/json'},
        data= json.dumps(post_data)
        )
    # Assert
    assert response.status_code == 200
    assert response.json() == response_data

def test_battle_victory_left():
    """
    Validation of battle in case of victory of the left pokemon
    """
    # Arrange
    post_data = {
            "pokemon_right": {
                "api_id": 5,
                "custom_name": "string",
                "id": 1,
                "name": "string",
                "trainer_id": 0
            },
            "pokemon_left": {
                "api_id": 20,
                "custom_name": "string",
                "id": 2,
                "name": "string",
                "trainer_id": 0
            }
        }
    response_data = {"winner": "1"}
    # Act
    response = client.post(
        "/battle/1/2",
        headers={'accept': 'application/json', 'Content-Type': 'application/json'},
        data= json.dumps(post_data)
        )
    # Assert
    assert response.status_code == 200
    assert response.json() == response_data

def test_battle_victory_right():
    """
    Validation of battle in case of victory of the right pokemon
    """
    # Arrange
    post_data = {
            "pokemon_right": {
                "api_id": 20,
                "custom_name": "string",
                "id": 1,
                "name": "string",
                "trainer_id": 0
            },
            "pokemon_left": {
                "api_id": 5,
                "custom_name": "string",
                "id": 2,
                "name": "string",
                "trainer_id": 0
            }
        }
    response_data = {"winner": "2"}
    # Act
    response = client.post(
        "/battle/1/2",
        headers={'accept': 'application/json', 'Content-Type': 'application/json'},
        data= json.dumps(post_data)
        )
    # Assert
    assert response.status_code == 200
    assert response.json() == response_data

