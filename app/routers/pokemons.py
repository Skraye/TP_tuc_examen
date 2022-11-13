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

@router.post("/{pokemon_id1}&{pokemon_id2}", response_model=List[schemas.Pokemon])
def battle_two_pokemons(pokemon_id1: int, pokemon_id2: int, pokemon1: schemas.Pokemon, pokemon2: schemas.Pokemon):
    """
        Does a battle between two pokemons
    """
    winner = battle_pokemon(pokemon_id1, pokemon_id2)
    return winner