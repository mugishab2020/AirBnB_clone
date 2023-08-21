import unittest
import os
from datetime import date, datetime
from models.base_model import BaseModel
import models

class TestBaseModel(unittest.TestCase):

    def test_init(self):
        #function for init
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_init_with_kwargs(self):
        #function test_init_with_kwargs
        data = {
            "id": "123",
            "created_at": "2023-01-01T00:00:00",
            "updated_at": "2023-01-02T00:00:00",
            "custom_attr": "test_value"
        }
        obj = BaseModel(**data)
        self.assertEqual(obj.id, "123")
        self.assertEqual(obj.custom_attr, "test_value")
        self.assertEqual(obj.created_at, datetime.fromisoformat("2023-01-01T00:00:00"))
        self.assertEqual(obj.updated_at, datetime.fromisoformat("2023-01-02T00:00:00"))

    def test_str(self):
        # function srt
        obj = BaseModel()
        string_representation = str(obj)
        self.assertIn("[BaseModel] ({})".format(obj.id), string_representation)

    def test_save(self):
        # function that test save
        obj = BaseModel()
        initial_updated_at = obj.updated_at
        self.assertIsNotNone(models.storage.all().get(obj.__class__.__name__ + "." + obj.id))

        obj.save()
        self.assertNotEqual(initial_updated_at, obj.updated_at)
        self.assertIsNotNone(models.storage.all().get(obj.__class__.__name__ + "." + obj.id))
        self.assertTrue(os.path.exists("file.json"))

    def test_to_dict(self):
        # function to change
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn("__class__", obj_dict)
        self.assertEqual(obj_dict["__class__"], "BaseModel")
        self.assertIsInstance(obj_dict["created_at"], str)
        self.assertIsInstance(obj_dict["updated_at"], str)

    def test_from_dict(self):
        # function to test dict
        data = {
            "id": "123",
            "created_at": "2023-01-01T00:00:00",
            "updated_at": "2023-01-02T00:00:00",
            "__class__": "BaseModel",
            "custom_attr": "test_value"
        }
        obj = BaseModel.from_dict(data)
        self.assertIsInstance(obj, BaseModel)
        self.assertEqual(obj.id, "123")
        self.assertEqual(obj.custom_attr, "test_value")
        self.assertEqual(obj.created_at, datetime.fromisoformat("2023-01-01T00:00:00"))
        self.assertEqual(obj.updated_at, datetime.fromisoformat("2023-01-02T00:00:00"))

if __name__ == "__main__":
    unittest.main()

