#!/usr/bin/python3
"""This module contains a base class called 'FileStorage' that defines
the process the serializes and deserializes to JSON
"""
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
        FileStorage.__objects[key_name]

    def save(self):
        pass

    def reload(self):
        pass
