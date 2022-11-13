"""Test pokeapi functions"""
import requests

BASE_URL = "https://pokeapi.co/api/v2"


def get_pokemon_name(api_id):
    """
        Get a pokemon name from the API pokeapi
    """
    return get_pokemon_data(api_id)['name']


def get_pokemon_data(api_id):
    """
        Get data of pokemon name from the API pokeapi
    """
    return requests.get(f"{BASE_URL}/pokemon/{api_id}", timeout=10).json()


def battle_pokemon(pokemon_1_api_id, pokemon_2_api_id):
    """
        Do battle between 2 pokemons
        return the name of the pokemon winner
    """
    premier_pokemon = get_pokemon_data(pokemon_1_api_id)
    second_pokemon = get_pokemon_data(pokemon_2_api_id)

    compteur_1 = 0
    compteur_2 = 0
    # Parcourir les stats des pokemons si  le Pokemon 1 > Pokemon 2  alors on rajoute +1 au compteur
    for i in range(min(len(premier_pokemon['stats']), len(second_pokemon['stats']))):
        if premier_pokemon['stats'][i]['base_stat'] > second_pokemon['stats'][i]['base_stat']:
            compteur_1 += 1
        elif premier_pokemon['stats'][i]['base_stat'] == second_pokemon['stats'][i]['base_stat']:
            pass
        else:
            compteur_2 += 1

    if compteur_1 > compteur_2:
        return premier_pokemon["forms"][0]['name']
    if compteur_1 == compteur_2:
        return premier_pokemon["forms"][0]['name'] + "égalité avec " + second_pokemon["forms"][0]['name']
    return second_pokemon["forms"][0]['name']
