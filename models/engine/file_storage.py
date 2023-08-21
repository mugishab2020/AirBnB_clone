#!/usr/bin/python3
""" created by Mugisha Prosper
    and Mugisha Edson as a collaborator
"""
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage(User):
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """ FileStorage constructor"""
        pass

    def all(self):
        """ Returns the dictionary objects"""
        return self.__objects

    def new(self, obj):
        """  sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        serialized_objs = {}
        for key, obj in self.__objects.items():
            serialized_objs[key] = obj.to_dict()

        with open(self.__file_path, "w") as file:
            json.dump(serialized_objs, file)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)
        """
        try:
            with open(self.__file_path, "r") as f:
                loaded_obj = json.load(f)

                for key, obj in loaded_obj.items():
                    class_name, obj_id = key.split('.')
                    obj_class = globals().get(class_name)
                    if obj_class:
                        self.__objects[key] = obj_class(**obj)
                    else:
                        pass
        except FileNotFoundError:
            pass
