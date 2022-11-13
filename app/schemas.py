"""Databse schemas"""
from datetime import date
from typing import List, Optional, Union
from pydantic import BaseModel

#
#  ITEM
#


class ItemBase(BaseModel):
    """ItemBase Class"""
    name: str
    description: Union[str, None] = None


class ItemCreate(ItemBase):
    """ItemCreate Class"""
    pass


class Item(ItemBase):
    """Item class"""
    id: int
    trainer_id: int

    class Config:
        """Config class"""
        orm_mode = True

#
#  POKEMON
#


class PokemonBase(BaseModel):
    """PokemonBase class"""
    api_id: int
    custom_name: Optional[str] = None


class PokemonCreate(PokemonBase):
    """PokemonCreate class"""
    pass


class Pokemon(PokemonBase):
    """Pokemon class"""
    id: int
    name: str
    trainer_id: int

    class Config:
        """Config class"""
        orm_mode = True
#
#  TRAINER
#


class TrainerBase(BaseModel):
    """TrainerBase class"""
    name: str
    birthdate: date


class TrainerCreate(TrainerBase):
    """TrainerCreate class"""
    pass


class Trainer(TrainerBase):
    """Trainer class"""
    id: int
    inventory: List[Item] = []
    pokemons: List[Pokemon] = []

    class Config:
        """Config class"""
        orm_mode = True
