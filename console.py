#!/usr/bin/python3
"""consol"""
import cmd
import models
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User
from datetime import datetime

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"
    intro = "Welcome to the HBNB command interpreter.Type 'help' to show all available commands."
    """clslist = {'BaseModel': BaseModel, 'State': State, 'City': City,
               'Amenity': Amenity, 'Place': Place, 'Review': Review,
               'User': User}"""
    def do_create(self, clsname =None):
        """Creates the new instance of the BaseModel
        save it and print its id"""
        if not clsname:
            print('** class name missing **')
        elif not sel.clslist.get(clsname):
            print('** class doesn\'t exist **')
        else:
            obj = sel.clslist[clsname]()
            models.storage.save()
            print(obj.id)
    def do_show(self, arg):
        """Show instance based on id"""
        clsname, objid = None, None
        args = arg.split(' ')
        if len(args) > 0:
            clsname = args[0]
        if len(args) > 1:
            objid = args[1]
        if not clsname:
            print('** class name missing **')
        elif not objid:
            print('** instance id missing **')
        elif not self.clslist.get(clsname):
            print("** class doesn't exist **")
        else:
            k = clsname + "." + objid
            obj = models.storage.all().get(k)
            if not obj:
                print('** no instance found **')
            else:
                print(obj)
    
    def do_destroy(self, arg):
        """destroy instance based on id
        """
        clsname, objid = None, None
        args = arg.split(' ')
        if len(args) > 0:
            clsname = args[0]
        if len(args) > 1:
            objid = args[1]
        if not clsname:
            print('** class name missing **')
        elif not objid:
            print('** instance id missing **')
        elif not self.clslist.get(clsname):
            print("** class doesn't exist **")
        else:
            k = clsname + "." + objid
            obj = models.storage.all().get(k)
            if not obj:
                print('** no instance found **')
            else:
                del models.storage.all()[k]
                models.storage.save()

    def do_all(self, arg):
        """Prints all instances based or not on the class name
        """
        if not arg:
            print([str(v) for k, v in models.storage.all().items()])
        else:
            if not self.clslist.get(arg):
                print("** class doesn't exist **")
                return False
            print([str(v) for k, v in models.storage.all().items()
                   if type(v) is self.clslist.get(arg)])
    def do_update(self, line):
        """
        Updates an instance by adding or updating attribute
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        obj = storage.all()
        objs_list = []
        for key in obj.keys():
            if (key.split(".")[0] not in objs_list):
                objs_list.append(key.split(".")[0])
        args = line.split(" ")
        if line == "":
            print("** class name missing **")
        elif args[0] not in objs_list:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            classname_id = args[0] + "." + args[1]
            if classname_id not in obj.keys():
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                objs = obj[classname_id]
                if args[3].startswith('"') and args[3].endswith('"'):
                    setattr(objs, args[2], str(args[3][1:-1]))
                elif args[3].startswith('"') and not args[3].endswith('"'):
                    str_value = ""
                    for arg in args[3:]:
                        str_value += " " + arg
                        if arg.endswith('"'):
                            break
                    print(str_value)
                    setattr(objs, args[2], str(str_value[2:-1]))
                elif "." in args[3]:
                    setattr(objs, args[2], float(args[3]))
                else:
                    setattr(objs, args[2], int(args[3]))
                storage.save()


    def do_quit(self,arg):
        """exiting the consol"""
        return True
    def do_EOF(self, arg):
        """exting also"""
        return True
    def empyline(self):
        """help command"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

