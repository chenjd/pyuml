import shlex

from typed_ast import ast3
from graphviz import Source

from core.parser import ClassParser
from core.basecmd import BaseCmd
from core.loader import Loader
from core.writer import DotWriter
from core.serializer import Serializer
from config.config import Config
from utilities.logger import Logger
from utilities.argument_parser import ArgumentParser


class PyUML(BaseCmd):

    def __init__(self):
        BaseCmd.__init__(self)
        self.prompt = "pyuml>>>"
        self.intro = """
//  
//                                  _oo8oo_
//                                 o8888888o
//                                 88" . "88
//                                 (| -_- |)
//                                 0\  =  /0
//                               ___/'==='\___
//                             .' \\|     |// '.
//                            / \\|||  :  |||// \\
//                           / _||||| -:- |||||_ \\
//                          |   | \\\  -  /// |   |
//                          | \_|  ''\---/''  |_/ |
//                          \  .-\__  '-'  __/-.  /
//                        ___'. .'  /--.--\  '. .'___
//                     ."" '<  '.___\_<|>_/___.'  >' "".
//                    | | :  `- \`.:`\ _ /`:.`/ -`  : | |
//                    \  \ `-.   \_ __\ /__ _/   .-` /  /
//                =====`-.____`.___ \_____/ ___.`____.-`=====
//                                  `=---=`
//  
//  
//       ~~~~~~above comments from https://github.com/ottomao/bugfreejs/blob/master/testFile_gbk.js have fun:)
//
//       ~~~~~~~Ara BCDE321 Assessment~~~~~~~~~~~~
//                
        """
        self.logger = Logger.get_instance().logging

    def do_exit(self, args):
        """
        Exit
        """
        return -1

    def do_version(self, args):
        """
        Print version info
        """
        config = Config()
        print("\nAra pyuml v" + config.version)

    def do_config(self, args):
        """
        Print config info
        """
        config = Config()
        print("\nAuthor: " + config.author)
        print("\nVersion: " + config.version)
        print("\nUrl: " + config.url)

    def do_2uml(self, args):
        """
        Generate UML diagram from Python source code
        """
        parser = ArgumentParser(prog='2uml', description='Generate UML diagram from Python source code')
        parser.add_argument('input', help='input file/folder')
        parser.add_argument('output', help='output folder')
        try:
            splitargs = parser.parse_args(shlex.split(args))

            input_path = splitargs.input
            output_path = splitargs.output
            loader = Loader()
            code_string_list = loader.load_from_file_or_directory(input_path)

            for index, code_string in enumerate(code_string_list):
                dot_string = self._parse_to_dot(code_string)
                self._render_with_graphviz(output_path, index, dot_string)

        except:
            print('Exception: Check the error log')
            self.logger.exception("2uml")
            pass

    def do_load(self, args):
        """
        Deserialize AST data from serialization data
        """
        parser = ArgumentParser(prog='load', description="Deserialize AST data from serialization data")
        parser.add_argument('input', help='input class name')

        try:
            splitargs = parser.parse_args(shlex.split(args))
            serializer = Serializer('artifacts', 'ast.db')
            result = serializer.deserilize(splitargs.input)
            print(result)

        except:
            print('Exception: Check the error log')
            self.logger.exception("load")
            pass

    def _parse_to_dot(self, code_string):
        """
        todo
        """
        class_parser = self._parse_to_class_recoard(code_string)
        self._persistent_to_file(class_parser.classes_list)
        dot_string = DotWriter().write(class_parser.classes_list)
        return dot_string

    def _persistent_to_file(self, obj_list):
        assert obj_list is not None
        serializer = Serializer('artifacts', 'ast.db')
        for obj in obj_list:
            serializer.serialize(obj)

    def _parse_to_class_recoard(self, code_string):
        tree = ast3.parse(code_string)
        class_parser = ClassParser()
        class_parser.visit(tree)
        return class_parser

    def _render_with_graphviz(self, output_path, index, dot):
        src = Source(dot)
        src.render(format='png', filename='uml{}'.format(index), directory=output_path)


if __name__ == '__main__':
    console = PyUML()
    console.cmdloop()
