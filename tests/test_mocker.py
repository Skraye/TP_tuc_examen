from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Combat pokemon
def test_pokemon_battle(mocker):
    """
        Resultat de la comparaison de stats
    """
    mocker.patch("app.utils.pokeapi.battle_compare_stats", return_value=1)
    response = client.get("/pokemons/battle/2/6")
    assert response.status_code == 200
    assert response.json() == {"pokemonApiID": 2, "result": 1}

# Combat pokemon
def test_pokemon_battle_draw(mocker):
    """
        Resultat de la comparaison de stats si egalite
    """
    mocker.patch("app.utils.pokeapi.battle_compare_stats", return_value=0)
    response = client.get("/pokemons/battle/2/6")
    assert response.status_code == 200
    assert response.json() == {"pokemonApiID": None, "result": 0}


# Create Pokemon For Trainer
def test_create_pokemon_for_trainer(mocker):
    """
        Creation d'un pokemon pour un trainer
    """
    nbPokemon = len(client.get("/pokemons").json())
    mocker.patch("app.utils.pokeapi.get_pokemon_data", return_value={"name": "ivysaur", "id": 2})
    response = client.post("/trainers/2/pokemon/", json={"api_id": 2, "custom_name": "Bulbi"})
    assert response.status_code == 200
    assert response.json() == {"api_id": 2, "custom_name": "Bulbi", "id": nbPokemon+1, "name": "ivysaur", "trainer_id": 2}


# Create Trainer
def test_create_trainer(mocker):
    """
        Creation d'un trainer
    """
    nbTrainer = len(client.get("/trainers").json())
    response = client.post("/trainers/", json={"name": "Mahat", "birthdate": "2022-11-07"})
    assert response.status_code == 200
    assert response.json() == {"name": "Mahat", "birthdate": "2022-11-07", "id": nbTrainer+1, "inventory": [], "pokemons": []}


# Create fake pokemon for trainer
def test_battle_fake_pokemon_for_trainer(mocker):
    """
        Creation d'un pokemon fake pour un trainer
    """
    mocker.patch("app.utils.pokeapi.get_pokemon_data", return_value=None)
    response = client.post("/trainers/2/pokemon/", json={"api_id": 0, "custom_name": "TheCreation"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Pokemon not found"}