#!/usr/bin/python3
"""
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """"""
    prompt = '(hbnb)'
    valid_classes = ['BaseModel']

    ERROR_CLASS_NAME = '** class name missing **'
    ERROR_CLASS = "** class doesn't exist **"
    ERROR_ID = "** instance id missing **"
    ERROR_ID_NOT_FOUND = "** no instance found **"
    ERROR_ATTR = "** attribute name missing **"
    ERROR_ATTR_VALUE = "** value missing **"

    def validate_len_args(self, arg):
        if len(arg) == 0:
            print(HBNBCommand.ERROR_CLASS_NAME)
            return False
        return True

    def validate_class_name(self, arg):
        args = arg.split(' ')
        class_name = args[0]
        if class_name not in HBNBCommand.valid_classes:
            print(HBNBCommand.ERROR_CLASS)
            return False
        return class_name

    def validate_id(self, arg):
        args = arg.split(' ')
        if len(args) < 2:
            print(HBNBCommand.ERROR_ID)
            return False
        id_number = args[1]
        return id_number

    def validate_attr(self, arg):
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

        my_model = BaseModel()
        my_model.save()
        print(my_model.id)

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
            print()

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
        if len(arg) > 0:
            class_name = self.validate_class_name(arg)
            if not class_name:
                return

        data_list = []
        for _, value in storage.all().items():
            data_list.append(str(value))

        print(data_list)

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
        attr_value :str= self.validate_attr_value(arg)
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

        print(type(attr_value))
        setattr(obj, attribute, attr_value)
        obj.save()
        # update BaseModel 7a9cfcec-b0bf-42b0-8fc5-f9d8318ccf54 first_name "Betty"


if __name__ == '__main__':
    HBNBCommand().cmdloop()
