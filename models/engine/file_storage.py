#!/usr/bin/python3
"""Module for FileStorage class."""
import json
from os import path
from models.user import User


class FileStorage:
    """Serializes instances to JSON file and deserializes to instances."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to JSON file (path: __file_path)."""
        obj_dict = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        if path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as file:
                obj_dict = json.load(file)
                for key, val in obj_dict.items():
                    cls_name, obj_id = key.split('.')
                    cls = globals()[cls_name]
                    obj = cls(**val)
                    self.new(obj)
