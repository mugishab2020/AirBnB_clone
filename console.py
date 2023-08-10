#!/usr/bin/python3
"""consol"""
import cmd
import models
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"
    intro = "Welcome to the HBNB command interpreter.Type 'help' to show all available commands."
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


    def do_quit(self,arg):
        """exiting the consol"""
        return True
    def do_EOF(self, arg):
        """exting also"""
        print()
        return True
    def empyline(self):
        """help command"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

