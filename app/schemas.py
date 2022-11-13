"""Module providingFunction printing python version."""
from datetime import date
from typing import List, Optional, Union
from pydantic import BaseModel

#
#  ITEM
#


class ItemBase(BaseModel):  # pylint: disable=too-few-public-methods
    """Class representing a person"""
    name: str
    description: Union[str, None] = None


class ItemCreate(ItemBase):  # pylint: disable=too-few-public-methods
    """Class representing a person"""


class Item(ItemBase):  # pylint: disable=too-few-public-methods
    """Class representing a person"""
    id: int
    trainer_id: int

    class Config:  # pylint: disable=too-few-public-methods
        """Class representing a person"""
        orm_mode = True

#
#  POKEMON
#


class PokemonBase(BaseModel):  # pylint: disable=too-few-public-methods
    """Class representing a person"""
    api_id: int
    custom_name: Optional[str] = None


class PokemonCreate(PokemonBase):  # pylint: disable=too-few-public-methods
    """Class representing a person"""


class Pokemon(PokemonBase):  # pylint: disable=too-few-public-methods
    """Class representing a person"""
    id: int
    name: str
    trainer_id: int

    class Config:  # pylint: disable=too-few-public-methods
        """Class representing a person"""
        orm_mode = True

#
#  TRAINER
#


class TrainerBase(BaseModel):  # pylint: disable=too-few-public-methods
    """Class representing a person"""
    name: str
    birthdate: date


class TrainerCreate(TrainerBase):  # pylint: disable=too-few-public-methods
    """Class representing a person"""


class Trainer(TrainerBase):  # pylint: disable=too-few-public-methods
    """Class representing a person"""
    id: int
    inventory: List[Item] = []
    pokemons: List[Pokemon] = []

    class Config:  # pylint: disable=too-few-public-methods
        """Class representing a person"""
        orm_mode = True

#
#  Battle
#


class BattleResult(BaseModel):  # pylint: disable=too-few-public-methods
    """Class representing a person"""
    winner: str
