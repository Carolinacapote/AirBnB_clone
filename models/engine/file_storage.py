#!/usr/bin/python3
"""This module contains a base class called 'FileStorage' that defines
the process the serializes and deserializes to JSON
"""
import json
import importlib
import re


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
        file_data = self.__deserialize()

        if not file_data:
            return

        for k, v in file_data.items():
            FileStorage.__objects[k] = self.choose_class(v["__class__"], v)

    def create(self, class_name):
        my_model = self.choose_class(class_name)
        my_model.save()
        print(my_model.id)

    def choose_class(self, class_name, data=None):
        module_name = self.__to_module_name(class_name)
        module = importlib.import_module(module_name)
        class_ = getattr(module, class_name)
        if data:
            return class_(**data)
        else:
            return class_()

        if class_name == 'BaseModel':
            from models.base_model import BaseModel
            return BaseModel(**data if data else None)
        elif class_name == 'User':
            from models.user import User
            return User(**data if data else None)
        elif class_name == 'Amenity':
            from models.amenity import Amenity
            return Amenity(**data if data else None)
        elif class_name == 'State':
            from models.state import State
            if data:
                return State(**data)
            else:
                return State()
        elif class_name == 'City':
            from models.city import City
            if data:
                return City(**data)
            else:
                return City()
        elif class_name == 'Place':
            from models.place import Place
            if data:
                return Place(**data)
            else:
                return Place()
        elif class_name == 'Review':
            from models.review import Review
            if data:
                return Review(**data)
            else:
                return Review()

    def print(self, class_name=None):
        print(self.filter_by_class(class_name))

    def filter_by_class(self, class_name):
        if not class_name:
            return self.to_list()

        filtered = []
        for k, value in self.all().items():
            split_key = k.split('.')
            if split_key[0] == class_name:
                filtered.append(str(value))
        return filtered

    def to_list(self):
        data_list = []
        for _, value in self.all().items():
            data_list.append(str(value))
        return data_list

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

    def __to_module_name(self, text):

        module_name = re.sub(r'(?<!^)(?=[A-Z])', '_', text).lower()
        return "models.{}".format(module_name)
