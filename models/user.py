#!/usr/bin/python3
""" UserClass """
from models.base_model import BaseModel


class User(BaseModel):
    """ User class that inherits Base Model """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
