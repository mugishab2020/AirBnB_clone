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

    def test_all(self):
        # test if initial 'all' return empty pbj
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

        obj_all = self.storage.all()
        self.assertIsInstance(obj_all, dict)
        self.assertEqual(len(obj_all), 0)

    def test_new_obj(self):
        """Function to test new obj"""
        obj = BaseModel()
        self.storage.new(obj)
        obj_all = self.storage.all()
        self.assertEqual(len(obj_all), 1)

        obj1 = BaseModel()
        obj2 = BaseModel()
        self.storage.new(obj1)
        self.storage.new(obj2)
        obj_all = self.storage.all()
        self.assertEqual(len(obj_all), 3)

    def test_save_and_reload(self):
        # function that test storage
        obj = BaseModel()

        # test when there is one element
        self.storage.new(obj)
        self.storage.save()

        new_storage = FileStorage()
        new_storage.reload()
        obj_all = new_storage.all()

        self.assertEqual(len(obj_all), 4)

        # test when there is more than one element
        self.storage.new(obj)
        self.storage.new(obj)
        self.storage.save()

        new_storage = FileStorage()
        new_storage.reload()
        obj_all = new_storage.all()

        self.assertEqual(len(obj_all), 4)

    def test_invalid_class_reload(self):
        # Test reloading with invalid reload
        with open(self.storage._FileStorage__file_path, 'w') as f:
            f.write('{"InvalidClass.123": {"id": "123"}}')

        self.storage.reload()
        all_objects = self.storage.all()
        self.assertEqual(len(all_objects), 0)

    def test_nonexistent_file_reload(self):
        # Test reloading with nonexistent JSON file (should be skipped)
        new_storage = FileStorage()
        new_storage._FileStorage__file_path = 'nonexistent.json'
        new_storage.reload()
        all_objects = new_storage.all()
        self.assertEqual(len(all_objects), 3)

    def test_none_file_path_reload(self):
        # Test reloading with file_path with none
        self.storage._FileStorage__file_path = None

        with self.assertRaises(TypeError):
            self.storage.reload()


if __name__ == "__main__":
    unittest.main()
