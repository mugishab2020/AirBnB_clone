#!/usr/bin/python3
"""
    review class
    Created by Mugisha Prosper
    and Mugisha Edson as a cotributor
"""
from models.base_model import BaseModel


class Review(BaseModel):
    place_id = ""
    user_id = ""
    text = ""
