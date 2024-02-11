#!/usr/bin/python3
"""Module creates a User class"""

from models.base_model import BaseModel


class City(BaseModel):
    """This Class for managing city objects"""

    state_id = ""
    name = ""
