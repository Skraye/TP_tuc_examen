"""Test trainers routes"""
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_trainers(mocker):
    """
        get all trainers
    """
    mocker.patch(
        "app.actions.get_trainers",
        return_value=[{"name": "Rémi", "birthdate": "2001-04-24", "id": 6, "inventory": [], "pokemons": []},
                      {"name": "Jaulin", "birthdate": "2001-01-16", "id": 5, "inventory": [], "pokemons": []}]
    )
    result = [{"name": "Rémi", "birthdate": "2001-04-24", "id": 6, "inventory": [], "pokemons": []},
              {"name": "Jaulin", "birthdate": "2001-01-16", "id": 5, "inventory": [], "pokemons": []}]

    response = client.get("/trainers")
    assert result == response.json()
    assert response.status_code == 200


def test_get_trainer(mocker):
    """
        get one trainer
    """
    trainer_id = 6
    mocker.patch(
        "app.actions.get_trainer",
        return_value={"name": "Rémi", "birthdate": "2001-04-24",
                      "id": trainer_id, "inventory": [], "pokemons": []}
    )
    result = {"name": "Rémi", "birthdate": "2001-04-24",
              "id": 6, "inventory": [], "pokemons": []}

    response = client.get(f"http://localhost:8000/trainers/{trainer_id}")
    assert result == response.json()
    assert response.status_code == 200
