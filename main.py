from source.components.dot_writer import DotWriter
from source.components.python_files_loader import PythonFilesLoader
from source.components.python_parser import PythonParser
from source.components.shelve_serializer import ShelveSerializer
from source.mvc.views.cmd_view import CmdView
from source.mvc.controllers.py_uml_controller import PyUmlController


if __name__ == '__main__':
    view = CmdView()
    dot_writer = DotWriter()
    python_parser = PythonParser()
    loader = PythonFilesLoader()
    serializer = ShelveSerializer('artifacts', 'ast.db')

    controller = PyUmlController(view,
                                 dot_writer,
                                 python_parser,
                                 loader,
                                 serializer)
    controller.run()
