import cmd
import argparse


class BaseCmd(cmd.Cmd):

    def __init__(self):
        cmd.Cmd.__init__(self)

    def do_help(self, args):
        """
        todo
        """
        cmd.Cmd.do_help(self, args)

    def emptyline(self):
        """
        todo
        """
        pass

    def default(self, line):
        """
        todo
        """
        print("Command not found\n")