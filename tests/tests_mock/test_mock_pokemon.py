"""Test pokemons routes"""
from fastapi.testclient import TestClient
from main import app
client = TestClient(app)


def test_get_pokemons(mocker):
    """
        get all pokemons
    """
    mocker.patch(
        "app.actions.get_pokemons",
        return_value=[{
            "api_id": 25,
            "custom_name": 'null',
            "id": 1,
            "name": "pikachu",
            "trainer_id": 1
        }, {
            "api_id": 3,
            "custom_name": 'null',
            "id": 2,
            "name": "venusaur",
            "trainer_id": 1
        }]
    )
    result = [{
        "api_id": 25,
        "custom_name": 'null',
        "id": 1,
        "name": "pikachu",
        "trainer_id": 1
    }, {
        "api_id": 3,
        "custom_name": 'null',
        "id": 2,
        "name": "venusaur",
        "trainer_id": 1
    }]

    response = client.get("/pokemons/")
    assert result == response.json()
    assert response.status_code == 200
