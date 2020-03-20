import argparse
import shlex
from core.parser import ClassParser
from core.basecmd import BaseCmd
from core.loader import Loader
from core.writer import DotWriter
from config import config

from typed_ast import ast3
from graphviz import Source

pyuml_version = "0.0.1"


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

    def do_exit(self, args):
        """
        todo
        """
        return -1

    def do_version(self, args):
        """
        todo
        """
        print("\nAra pyuml v" + pyuml_version)
        print("by chenjd and liam\n")

    def do_2uml(self, args):
        """
        Generate UML diagram from Python source code
        """
        parser = argparse.ArgumentParser(prog='2uml')
        parser.add_argument('Input', help='input file')
        parser.add_argument('Output', help='output file')
        try:
            splitargs = parser.parse_args(shlex.split(args))
            dot_string = self._parse_to_dot(splitargs.Input)
            self._render_with_graphviz(dot_string)
        except:
            pass

    def _parse_to_dot(self, args):
        """
        todo
        """
        loader = Loader()
        code_string = loader.load_from_file(args)
        tree = ast3.parse(code_string)
        class_parser = ClassParser()
        class_parser.visit(tree)
        print(class_parser.classes_list)

        dot_string = DotWriter().write(class_parser.classes_list)
        return dot_string

    def _render_with_graphviz(self, dot):
        src = Source(dot)
        src.render(format='png', filename="result/uml")

    def do_persistent(self, args):
        """
        Generate serialization data from AST obj.
        """
        parser = argparse.ArgumentParser(prog='read')
        parser.add_argument('Input', help='input file')
        parser.add_argument('Output', help='output file')
        try:
            splitargs = parser.parse_args(shlex.split(args))

        except Exception as e:
            print("ERROR", e)

    def do_load(self, args):
        """
        Deserialize AST data from serialization data
        """
        parser = argparse.ArgumentParser(prog='read')
        parser.add_argument('Input', help='input file')
        parser.add_argument('Output', help='output file')

        try:
            splitargs = parser.parse_args(shlex.split(args))

        except Exception as e:
            print("ERROR", e)


if __name__ == '__main__':
    console = PyUML()
    console.cmdloop()
