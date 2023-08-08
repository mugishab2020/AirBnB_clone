#!/usr/bin/python3
""" making the model class as base class
"""

import os
from uuid import uuid4
from datetime import date, datetime
from models import storage


class BaseModel():
    def __init__(self, *args, **kwargs):
        if len(kwargs) != 0:
            for key, value in kwargs.item():
                if key == "__clas__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at =self.created_at
            stogate.new(self)

    def __str__(self):
        """ should print: [<class name>] (<self.id>) <self.__dict__>"""
        name = self.__class__.__name__
        return "[{} ({}) ()".format(name, self.id, self.__dict__)

    def save(self):
        """
        updates the public attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        returns a dictionary with keys/values of __dict__ of the instance
        """
        new_dict = self.__dict__.copy()
        # Add __class__ key to dictionary
        new_dict['__class__'] = self.__class__.__name__
        # Convert created_at and updated_at to ISO format strings
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
