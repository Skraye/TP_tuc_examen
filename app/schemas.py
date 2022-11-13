from datetime import date
from typing import  List, Optional, Union
from pydantic import BaseModel

#
#  ITEM
#
class ItemBase(BaseModel):
    """
        Class for item base model
    """
    name: str
    description: Union[str, None] = None

class ItemCreate(ItemBase):
    """
        Class for item creation
    """
    created:bool
    pass

class Item(ItemBase):
    """
        Class for item model
    """
    id: int
    trainer_id: int

    class Config:
        orm_mode = True

#
#  POKEMON
#
class PokemonBase(BaseModel):
    """
        Class for pokemon base model
    """
    api_id: int
    custom_name: Optional[str] = None

class PokemonCreate(PokemonBase):
    """
        Class for pokemon creation
    """
    pass

class Pokemon(PokemonBase):
    """
        Class for pokemon model
    """
    id: int
    name: str
    trainer_id: int

    class Config:
        orm_mode = True
#
#  TRAINER
#
class TrainerBase(BaseModel):
    """
        Class for trainer base model
    """
    name: str
    birthdate: date

class TrainerCreate(TrainerBase):
    """
        Class for trainer creation
    """
    pass

class Trainer(TrainerBase):
    """
        Class for trainer model
    """
    id: int
    inventory: List[Item] = []
    pokemons: List[Pokemon] = []

    class Config:
        orm_mode = True

class Battle(BaseModel):
    """
        Initialized a simple battle class for result purposes
    """
    winner:str
