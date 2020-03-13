import ast
from lib.parser import ClassParser
from lib.basecmd import BaseCmd
import typed_ast

pyuml_version = "0.0.1"


class PyUML(BaseCmd):

    def __init__(self):
        BaseCmd.__init__(self, None)
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

    def do_exit(self, _args):
        """
        todo
        """
        return -1

    def do_version(self, args):
        """
        todo
        """
        print("\nAra pyuml v" + pyuml_version)
        print("by chenjd\n")

    def do_parse(self, args):
        """
        todo
        """
        print(args)
        tree = ast.parse(args)
        print(tree)
        result = ClassParser().visit_ClassDef(tree)
        print(result)





if __name__ == '__main__':
    console = PyUML()
    console.cmdloop()
