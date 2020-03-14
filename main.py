import ast
from utils.parser import ClassParser
from utils.basecmd import BaseCmd
from utils.loader import Loader
from typed_ast import ast3

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

    def do_parse(self, args):
        """
        todo
        """
        loader = Loader()
        code_string = loader.load_from_file(args)
        tree = ast3.parse(code_string)
        result = ClassParser().visit(tree)


if __name__ == '__main__':
    console = PyUML()
    console.cmdloop()
