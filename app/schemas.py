from datetime import date
from typing import  List, Optional, Union
from pydantic import BaseModel

#
#  ITEM
#
class ItemBase(BaseModel):
    name: str
    description: Union[str, None] = None

class ItemCreate(ItemBase):
    """
    Creation item
    """

class Item(ItemBase):
    id: int
    trainer_id: int

    class Config:
        orm_mode = True

#
#  POKEMON
#
class PokemonBase(BaseModel):
    api_id: int
    custom_name: Optional[str] = None

class PokemonCreate(PokemonBase):
    """
    creation pokemon
    """

class Pokemon(PokemonBase):
    id: int
    name: str
    trainer_id: int

    class Config:
        orm_mode = True
#
#  TRAINER
#
class TrainerBase(BaseModel):
    name: str
    birthdate: date

class TrainerCreate(TrainerBase):
    """
    creation trainer
    """

class Trainer(TrainerBase):
    id: int
    inventory: List[Item] = []
    pokemons: List[Pokemon] = []

    class Config:
        orm_mode = True
