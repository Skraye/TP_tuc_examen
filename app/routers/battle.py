"""Module providingFunction printing python version."""
from fastapi import APIRouter
from ..utils import pokeapi
from .. import schemas
router = APIRouter()


@router.post("/{pokemon_right_id}/{pokemon_left_id}", response_model=schemas.BattleResult)
def battle(pokemon_right_id: int,pokemon_left_id: int,pokemon_right: schemas.Pokemon, pokemon_left: schemas.Pokemon):
    """
        Do battle between 2 trainer
    """
    pokemon_victorieux = pokeapi.battle_pokemon(
        pokemon_right.api_id, pokemon_left.api_id)
    print(pokemon_victorieux)
    if pokemon_victorieux['winner'] == "right":
        pokemon_victorieux['winner'] = str(pokemon_right_id)
        return pokemon_victorieux
    if pokemon_victorieux['winner'] == "left":
        pokemon_victorieux['winner'] = str(pokemon_left_id)
        return pokemon_victorieux
    return pokemon_victorieux
