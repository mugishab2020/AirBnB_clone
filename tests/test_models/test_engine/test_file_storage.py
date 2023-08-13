#!usr/bin/python3
"""
    models/engine/file_storage.py test file
    created by Mugisha Prosper
    and Mugisha Edson as contributor
"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os


class TestFileStorage(unittest.TestCase):
    """ models/engine/file_storage.py test file"""
    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        # run at exist of every function
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_new_obj(self):
        """Function to test new obj"""
        obj = BaseModel()
        self.storage.new(obj)
        self.assertIn(f"{obj.__class__.__name__}.{obj.id}", self.storage.all())

    def test_save_and_reload(self):
        # function that test storage
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()

        new_storage = FileStorage()
        new_storage.reload()

        self.assertIn(f"{obj.__class__.__name__}.{obj.id}", new_storage.all())


if __name__ == "__main__":
    unittest.main()
