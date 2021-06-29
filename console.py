#!/usr/bin/python3
"""Program called console.py that contains the entry point of the command
interpreter.
"""
import cmd
import os
from models.base_model import BaseModel
from models import storage

# TODO: refactor delete, create, update, print in storage
class HBNBCommand(cmd.Cmd):
    """Class to manage the console and all the commands built to the project"""
    prompt = '(hbnb)'
    valid_classes = ['BaseModel', 'User', 'Amenity', 'Review', 'State', 'City',
                     'Place']

    ERROR_CLASS_NAME = '** class name missing **'
    ERROR_CLASS = "** class doesn't exist **"
    ERROR_ID = "** instance id missing **"
    ERROR_ID_NOT_FOUND = "** no instance found **"
    ERROR_ATTR = "** attribute name missing **"
    ERROR_ATTR_VALUE = "** value missing **"

    def validate_len_args(self, arg):
        """Validates if the command receives the class_name argument"""
        if len(arg) == 0:
            print(HBNBCommand.ERROR_CLASS_NAME)
            return False
        return True

    def validate_class_name(self, arg):
        """Validates if the class_name argument is a valid class"""
        args = arg.split(' ')
        class_name = args[0]
        if class_name not in HBNBCommand.valid_classes:
            print(HBNBCommand.ERROR_CLASS)
            return False
        return class_name

    def validate_id(self, arg):
        """Validates if the command receives an id_number argument """
        args = arg.split(' ')
        if len(args) < 2:
            print(HBNBCommand.ERROR_ID)
            return False
        id_number = args[1]
        return id_number

    def validate_attr(self, arg):
        """Validates if the command receives an attribute argu"""
        args = arg.split(' ')
        if len(args) < 3:
            print(HBNBCommand.ERROR_ATTR)
            return False
        attribute = args[2]
        return attribute

    def validate_attr_value(self, arg):
        args = arg.split(' ')
        if len(args) < 4:
            print(HBNBCommand.ERROR_ATTR_VALUE)
            return False
        attr_value = args[3]
        return attr_value

    def do_EOF(self, arg):
        """ Quit with new line """
        print()
        return True

    def emptyline(self):
        pass

    def do_quit(self, arg):
        """ quit you tty"""
        return True

    def do_create(self, arg):
        if not self.validate_len_args(arg):
            return

        class_name = self.validate_class_name(arg)
        if not class_name:
            return

        storage.create(class_name)

    def do_show(self, arg):
        if not self.validate_len_args(arg):
            return

        class_name = self.validate_class_name(arg)
        if not class_name:
            return

        id_number = self.validate_id(arg)
        if not id_number:
            return
        objects = storage.all()
        key = "{}.{}".format(class_name, id_number)
        try:
            print(objects[key])
        except:
            print(HBNBCommand.ERROR_ID_NOT_FOUND)

    def do_destroy(self, arg):
        if not self.validate_len_args(arg):
            return

        class_name = self.validate_class_name(arg)
        if not class_name:
            return

        id_number = self.validate_id(arg)
        if not id_number:
            return

        objects = storage.all()
        key = "{}.{}".format(class_name, id_number)

        try:
            del objects[key]
            storage.save()
        except:
            print(HBNBCommand.ERROR_ID_NOT_FOUND)

    def do_all(self, arg):
        class_name = None
        if len(arg) > 0:
            class_name = self.validate_class_name(arg)
            if not class_name:
                return
            # filter data
        storage.print(class_name)

    def do_update(self, arg):
        if not self.validate_len_args(arg):
            return
        class_name = self.validate_class_name(arg)
        if not class_name:
            return
        id_number = self.validate_id(arg)
        if not id_number:
            return

        attribute = self.validate_attr(arg)
        if not attribute:
            return
        attr_value = self.validate_attr_value(arg)
        if not attr_value:
            return
        try:
            objects = storage.all()
            key = "{}.{}".format(class_name, id_number)
            obj = objects[key]
        except:
            print(HBNBCommand.ERROR_ID_NOT_FOUND)
            return

        # obj[attribute] = attr_value
        attr_value = attr_value.strip('"')

        if attr_value.isdigit():
            attr_value = int(attr_value)
        else:
            try:
                attr_value = float(attr_value)
            except:
                pass

        setattr(obj, attribute, attr_value)
        obj.save()

    def do_clear(self, _):
        if os.name == 'posix':
            os.system('clear')
        else:
            os.system('cls')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
