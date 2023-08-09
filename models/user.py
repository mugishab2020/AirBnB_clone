#!/usr/bin/python3
"""
    User class
    created by Mugisha Prosper and
    Mugisha Edson as a collaborator

"""
from models.base_model import BaseModel


class User(BaseModel):
    """ a user class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
