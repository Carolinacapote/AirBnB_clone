#!/usr"""/bin/python3
"""This module contains a base class called 'BaseModel'that defines all common
attributes/methods for other classes.
"""
import uuid
import datetime


class BaseModel:
    """
    Public instance attributes:
        id (str):  assign with an uuid when an instance is created.
        created_at: current datetime when an instance is created
        updated_at: current datetime when an instance is created and it will
        be updated every time the object changes.
    """

    def __init__(self):

        # UUID
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """Overriding the __str__ method
        Returns:
            Information with this format:
            [<class name>] (<self.id>) <self.__dict__>
        """
        to_print = '[{}] ({}) {}'.format(__class__.__name__, self.id,
                                         self.__dict__)
        return to_print

    def save(self):
        """"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        Returns:
            -A dictionary containing keys/values of __dict__ of the instance
            -A 'key __class__'  with the class name of the object.
            -'created_at' and 'updated_at' in isoformat()
        """
        my_dict = self.__dict__
        my_dict['__class__'] = __class__.__name__
        my_dict['updated_at'] = self.updated_at.isoformat()
        my_dict['created_at'] = self.created_at.isoformat()
        return my_dict
