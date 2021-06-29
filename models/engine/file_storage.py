#!/usr/bin/python3
"""This module contains a base class called 'FileStorage' that defines
the process the serializes and deserializes to JSON
"""
from datetime import datetime
import json



class FileStorage:
    """"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        key_name = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key_name] = obj

    def save(self):
        content = self.__serialize()

        with open(FileStorage.__file_path, 'w') as file:
            file.write(content)

    def reload(self):
        from models.base_model import BaseModel
        file_data = self.__deserialize()

        if not file_data:
            return

        for k, v in file_data.items():
            if v['__class__'] == 'BaseModel':
                FileStorage.__objects[k] = BaseModel(**v)
            elif v['__class__'] == 'User':
                from models.user import User
                FileStorage.__objects[k] = User(**v)

    def __serialize(self):
        """
        BaseModel->to_dict() -> <class 'dict'> -> JSON dump -> <class 'str'>
        """
        objects = {}
        for key, obj in self.all().items():
            objects[key] = obj.to_dict()

        return str(json.dumps(objects))

    def __deserialize(self):
        try:
            with open(FileStorage.__file_path) as file:
                return json.load(file)
        except:
            pass
