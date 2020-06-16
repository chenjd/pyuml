from mvc.controllers.py_uml_controller import PyUmlController
from mvc.views.cmd_view import CmdView
from utilities.logger import Logger


if __name__ == '__main__':
    controller = PyUmlController(CmdView())
    controller.run()
