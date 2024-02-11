#!/usr/bin/python3
"""Module creates a Review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """This Class for managing review objects"""

    place_id = ""
    user_id = ""
    text = ""
