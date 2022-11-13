"""Pokemons routes"""
from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter,  Depends
from app import actions, schemas
from app.utils.utils import get_db
from app.actions import get_pokemon
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


@router.get("/battle/{first_pokemon_id}/{second_pokemon_id}")
def get_battle_pokemon(first_pokemon_id: int, second_pokemon_id: int, database: Session = Depends(get_db)):
    """
       battle between 2 pokemon
    """

    pokemon_1 = get_pokemon(database, pokemon_id=first_pokemon_id)
    pokemon_2 = get_pokemon(database, pokemon_id=second_pokemon_id)

    battle = battle_pokemon(pokemon_1.api_id, pokemon_2.api_id)

    return battle
