import cmd
import shlex
from source.mvc.views.base_view import BaseView
from source.mvc.events.ui_event import UIEvent
from source.mvc.events.ui_event_type import UIEventType
from source.utilities.argument_parser import ArgumentParser
from source.utilities.logger import Logger


class CmdView(cmd.Cmd, BaseView):
    def __init__(self):
        cmd.Cmd.__init__(self)
        BaseView.__init__(self)
        self.prompt = "pyuml>>>"
        self.intro = "This is PyUML..."
        self.logger = Logger.get_instance().logging
        self.__view_type = 'cmd_view'

    def start(self):  # pragma: no cover
        self.cmdloop()

    def stop(self):
        exit()

    def view_print(self, content: str):
        print("{}: {}".format(self.__view_type, content))

    def do_exit(self, args):
        """
        Exit
        """
        self.notify(UIEvent(UIEventType.EXIT))

    def do_version(self, args):
        """
        Print version info
        """
        self.notify(UIEvent(UIEventType.VERSION))

    def do_config(self, args):
        """
        Print config info
        """
        self.notify(UIEvent(UIEventType.CONFIG))

    def do_2uml(self, args):
        """
        Generate UML diagram from Python source code
        """
        parser = ArgumentParser(prog='2uml',
                                description='Generate UML diagram'
                                            ' from Python source code')
        parser.add_argument('input', help='input file/folder')
        parser.add_argument('output', help='output folder')
        try:
            split_args = parser.parse_args(shlex.split(args, posix=0))
            self.notify(UIEvent(UIEventType.UML, split_args))
        except (AttributeError, IOError, SystemExit) as e:
            print('Exception: Check the error log')
            self.logger.exception("2uml")

    def do_load(self, args):
        """
        Deserialize AST data from serialization data
        """
        parser = ArgumentParser(prog='load',
                                description="Deserialize AST data"
                                            " from serialization data")
        parser.add_argument('input', help='input class name')

        try:
            split_args = parser.parse_args(shlex.split(args, posix=0))
            self.notify(UIEvent(UIEventType.LOAD, split_args))

        except (AttributeError, IOError, SystemExit, KeyError) as e:
            print('Exception: Check the error log')
            self.logger.exception("load")
            pass

    def do_help(self, args):  # pragma: no cover
        """
        Help Information
        """
        cmd.Cmd.do_help(self, args)

    def default(self, line):  # pragma: no cover
        """
        todo
        """
        print("Command not found\n")
