#/usr/bin/python3
""" created by Mugisha Prosper
    and Mugisha Edson as a collaborator
"""
import json


class FileStorage:
    __file_path
    __objects

    __init__(self):
        """ FileStorage constructor"""
        pass

    def all(self):
        """ Returns the dictionary objects"""
        pass

    def new(self, obj):
        """  sets in __objects the obj with key <obj class name>.id"""
        pass

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        pass

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file doesn’t exist, no exception should be raised)
        """
        pass


