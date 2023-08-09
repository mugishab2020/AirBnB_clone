#!/usr/bin/python3
""" created by Mugisha Prosper
    and Mugisha Edson as a collaborator
"""
import json


class FileStorage:
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
        serialized_obj = {}
        for key, obj in self.__objects.items():
            serialized_obj[key] = obj.to_dict()

        try:
            with open(self.__file_path, "a") as file:
                json.dump(serialized_obj, file)
                file.write("\n")
        except FileNotFoundError:
            with open(self.__file_path, "w") as file:
                json.dump(serialized_obj, file)
                file.write("\n")

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)
        """
        try:
            with open(self.__file_name, "r") as data:
                loaded_obj = json.load(data)

                for key, obj in loaded_obj.items():
                    class_name, obj_id = key.split('.')
                    self.__objects[key] = globals()[class_name](**obj)
        except FileNotFoundError:
            pass
