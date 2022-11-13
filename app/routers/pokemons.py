from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter,  Depends
from app import actions, schemas
from app.utils.utils import get_db
from app.utils.pokeapi import battle_pokemon

router = APIRouter()


@router.get("/", response_model=List[schemas.Pokemon])
def get_pokemons(skip: int = 0, limit: int = 100, database: Session = Depends(get_db)):
    """
        Return all pokemons
        Default limit is 100
    """
    pokemons = actions.get_pokemons(database, skip=skip, limit=limit)
    return pokemons

@router.post("/", response_model = List[schemas.Battle])
def duel_pokemons(pokemon1: schemas.Pokemon, pokemon2: schemas.Pokemon, poke1_id:int, poke2_id:int):
    """
        Does a battle between 2 pokemons
    """
    winner = battle_pokemon(pokemon1.api_id, pokemon2.api_id)
    if winner['winner'] == poke1_id:
        winner['winner'] = str(poke1_id)
    elif winner['winner'] == poke2_id:
        winner['winner'] = str(poke2_id)
    return winner
