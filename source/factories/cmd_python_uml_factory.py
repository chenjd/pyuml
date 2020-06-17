from source.components.dot_writer import DotWriter
from source.components.python_files_loader import PythonFilesLoader
from source.components.python_parser import PythonParser
from source.components.shelve_serializer import ShelveSerializer
from source.factories.abstract_factory import AbstractFactory
from source.mvc.controllers.py_uml_controller import PyUmlController
from source.mvc.views.cmd_view import CmdView


class CmdPythonUmlFactory(AbstractFactory):
    def create_view(self):
        return CmdView()

    def create_controller(self, view):
        dot_writer = DotWriter()
        python_parser = PythonParser()
        loader = PythonFilesLoader()
        serializer = ShelveSerializer('artifacts', 'ast.db')

        return PyUmlController(view,
                               dot_writer,
                               python_parser,
                               loader,
                               serializer)
