import json
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_pokemons(mocker):
    #Given/When
    with open('../resources/pokemon.json', encoding='utf-8') as data_raw:
        data = json.load(data_raw)
        mocker.patch(
        "app.actions.get_pokemons",
        return_value= data
        )
    response = client.get("pokemons/?skip=0&limit=100")

    #Then
    assert response.status_code == 200
    assert response.json() == data
