#!/usr/bin/python3
"""
    This is a module test from BaseModel class and your methods.
"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """
    this class test user class and your behavior
    """

    def setUp(self):
        self.user = User()

    def test_creation(self):
        '''this test validate that creation proccess was correct.
        '''
        self.assertEqual(self.user.first_name, '')
