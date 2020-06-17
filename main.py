from source.factories.abstract_factory import AbstractFactory
from source.factories.cmd_python_uml_factory import CmdPythonUmlFactory
from source.mvc.controllers.base_controller import BaseController
from source.mvc.views.base_view import BaseView


class PyUML:
    def __init__(self, factory: AbstractFactory):
        self.__view: BaseView = factory.create_view()
        self.__controller: BaseController = \
            factory.create_controller(self.__view)

    def run(self):
        self.__controller.run()


if __name__ == '__main__':
    client = PyUML(CmdPythonUmlFactory())
    client.run()
