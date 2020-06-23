import os
import pathlib

from source.components.dot_writer import DotWriter
from source.components.python_files_loader import PythonFilesLoader
from source.components.python_parser import PythonParser
from source.components.shelve_serializer import ShelveSerializer
from source.factories.abstract_factory import AbstractFactory
from source.mvc.controllers.py_uml_controller import PyUmlController
from source.mvc.views.cmd_view import CmdView
from source.mvc.models.class_recorder import ClassRecorder


class CmdPythonUmlFactory(AbstractFactory):
    def create_view(self):
        return CmdView()

    def create_controller(self, view):
        dot_writer = DotWriter()
        python_parser = PythonParser(ClassRecorder)
        loader = PythonFilesLoader()
        root_dir = pathlib.Path(__file__).parent.absolute()
        artifact_dir = os.path.join(root_dir, 'artifacts')
        serializer = ShelveSerializer(artifact_dir, 'ast.db')

        return PyUmlController(view,
                               dot_writer,
                               python_parser,
                               loader,
                               serializer)
