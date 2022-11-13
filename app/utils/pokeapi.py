import requests

BASE_URL = "https://pokeapi.co/api/v2"


def get_pokemon_name(api_id):
    """
        Get a pokemon name from the API pokeapi
    """
    return get_pokemon_data(api_id)['name']

def get_pokemon_stats(api_id):
    """
        Get pokemon stats from the pokeapi API
    """
    #Nous avons choisi que 4 stats par pokemon
    pokemon_data = get_pokemon_data(api_id)

    pokemon_stats = {
        pokemon_data["stats"][0]["stat"]["name"]:
        pokemon_data["stats"][0]["base_stat"],    #HP
        pokemon_data["stats"][1]["stat"]["name"]:
        pokemon_data["stats"][0]["base_stat"],    #Attack
        pokemon_data["stats"][2]["stat"]["name"]:
        pokemon_data["stats"][0]["base_stat"],    #Defense
        pokemon_data["stats"][3]["stat"]["name"]:
        pokemon_data["stats"][0]["base_stat"],    #Special attack
        pokemon_data["stats"][4]["stat"]["name"]:
        pokemon_data["stats"][0]["base_stat"],    #Special defense
        pokemon_data["stats"][5]["stat"]["name"]:
        pokemon_data["stats"][0]["base_stat"]     #Speed
    }

    return pokemon_stats

def get_pokemon_data(api_id):
    """
        Get data of pokemon name from the API pokeapi
    """
    return requests.get(f"{BASE_URL}/pokemon/{api_id}", timeout=10).json()


def battle_pokemon(first_api_id, second_api_id):
    """
        Do battle between 2 pokemons
    """

    first_pokemon = get_pokemon_stats(first_api_id)
    second_pokemon = get_pokemon_stats(second_api_id)
    battle_result = battle_compare_stats(first_pokemon, second_pokemon)

    return ({'winner' : first_pokemon} if battle_result > 0
    else {'winner' : second_pokemon} if battle_result < 0
    else {'winner' : 'draw'})


def battle_compare_stats(pokemon_stats_1, pokemon_stats_2):
    """
        Compare given stats between 2 pokemons
    """
    result = 0

    for stat in pokemon_stats_1:
        if pokemon_stats_1[stat] > pokemon_stats_2[stat]:
            result += 1
        elif pokemon_stats_1[stat] < pokemon_stats_2[stat]:
            result -= 1
        else:
            continue
    return result
