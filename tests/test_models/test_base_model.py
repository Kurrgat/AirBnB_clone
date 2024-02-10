#!/usr/bin/python3
"""
This module contains the unit tests for the BaseModel class.
"""

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class.
    """

    def test_init(self):
        """
        Test the __init__ method of BaseModel.
        """
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        self.assertTrue(hasattr(my_model, "id"))
        self.assertTrue(hasattr(my_model, "created_at"))
        self.assertTrue(hasattr(my_model, "updated_at"))
        self.assertNotEqual(my_model.id, "")
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_str(self):
        """
        Test the __str__ method of BaseModel.
        """
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        expected_str = "[BaseModel] ({}) {}".format(my_model.id, my_model.__dict__)
        self.assertEqual(str(my_model), expected_str)

    def test_save(self):
        """
        Test the save method of BaseModel.
        """
        my_model = BaseModel()
        old_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(old_updated_at, my_model.updated_at)

    def test_to_dict(self):
        """
        Test the to_dict method of BaseModel.
        """
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()
        self.assertEqual(my_model_json["__class__"], "BaseModel")
        self.assertEqual(my_model_json["name"], "My First Model")
        self.assertEqual(my_model_json["my_number"], 89)
        self.assertTrue("created_at" in my_model_json)
        self.assertTrue("updated_at" in my_model_json)
        self.assertIsInstance(my_model_json["created_at"], str)
        self.assertIsInstance(my_model_json["updated_at"], str)


if __name__ == "__main__":
    unittest.main()

