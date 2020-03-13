import cmd
import argparse


class BaseCmd(cmd.Cmd):

    def __init__(self, session):
        cmd.Cmd.__init__(self)

    def do_help(self, args):
        """
        todo
        """
        cmd.Cmd.do_help(self, args)
        # parser = argparse.ArgumentParser(prog = 'pyuml', add_help = False)
        # parser.add_argument('-i', help='input')
        # parser.add_argument('-o', help='output')
        # parser.print_help()

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