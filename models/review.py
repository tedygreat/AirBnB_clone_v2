#!/usr/bin/python3
""" ClassReview """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class that inherits Base Model """
    place_id = ""
    user_id = ""
    text = ""
