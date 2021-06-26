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

    def do_EOF(self, arg):
        """ Quit with new line """
        print()
        return True

    def emptyline(self):
        pass

    def do_capote(self, arg):
        """ I'm capote method """
        print('Yo soy capote')

    def do_quit(self, arg):
        """ quit you tty"""
        return True

    def do_create(self, arg):
        if len(arg) == 0:
            print('** class name missing **')
            return

        args = arg.split(' ')
        class_name = args[0]

        if class_name not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
            return

        my_model = BaseModel()
        my_model.save()
        print(my_model.id)

    def do_show(self, arg):
        if len(arg) == 0:
            print('** class name missing **')
            return

        args = arg.split(' ')
        length = len(args)
        class_name = args[0]

        if class_name not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
            return

        if length < 2:
            print("** instance id missing **")
            return

        id_number = args[1]

        objects = storage.all()
        key = "{}.{}".format(class_name, id_number)

        try:
            print(objects[key])
        except:
            print("** no instance found **")
        # objects[BaseModel.21397971293]

    def do_destroy(self, arg):
        if len(arg) == 0:
            print('** class name missing **')
            return
        args = arg.split(' ')
        length = len(args)
        class_name = args[0]

        if class_name not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
            return

        if length < 2:
            print("** instance id missing **")
            return

        id_number = args[1]

        objects = storage.all()
        key = "{}.{}".format(class_name, id_number)

        try:
            del objects[key]
            storage.save()
        except:
            print("** no instance found **")

    def do_all(self, arg):
        pass

    def do_update(self, arg):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
