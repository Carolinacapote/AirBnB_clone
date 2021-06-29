#!/usr/bin/python3
"""This module contains a base class called 'BaseModel'that defines all common
attributes/methods for other classes.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Public class attributes:
        email: string - empty string
        password: string - empty string
        first_name: string - empty string
        last_name: string - empty string
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        if len(kwargs) == 0:
            super().__init__()

        # if kwargs have values
        if len(kwargs) > 0:
            super().__init__(**kwargs)

    def __str__(self):
        """Overriding the __str__ method
        Returns:
            Information with this format:
            [<class name>] (<self.id>) <self.__dict__>
        """
        my_dict = self.__dict__

        my_dict['updated_at'] = self.updated_at
        my_dict['created_at'] = self.created_at
        to_print = '[{}] ({}) {}'.format(__class__.__name__, self.id,
                                         my_dict)
        return to_print


    def to_dict(self):
        my_dict = super().to_dict()
        my_dict['__class__'] = 'User'
        return my_dict
