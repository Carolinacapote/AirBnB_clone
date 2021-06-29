#!/usr/bin/python3
# '''
#     module documentation
# '''
# import unittest
# from models.base_model import BaseModel
# import os
# import sys
# from console import HBNBCommand
# from io import StringIO


# class TestConsole(unittest.TestCase):

#     def setUp(self) -> None:
#         return super().setUp()

#     def out_test(self, func, arg, expect):
#         std_out = StringIO()
#         sys.stdout = std_out
#         func(arg)
#         output = std_out.getvalue()
#         self.assertEqual(output, expect + '\n')
#         return output

#     def test_creation_failed(self):
#         ''' creation test '''
#         try:
#             os.remove('file.json')
#         except:
#             pass
#         cmd = HBNBCommand()

#         self.out_test(cmd.do_create, '', HBNBCommand.ERROR_CLASS_NAME)
#         self.out_test(cmd.do_create, 'myModel', HBNBCommand.ERROR_CLASS)

#     def test_create_ok(self):
#         cmd = HBNBCommand()
#         out = self.out_test(cmd.do_create, 'BaseModel', '')
