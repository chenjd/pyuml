from graphviz import Source
from typed_ast import ast3

from source.components.base_loader import BaseLoader
from source.components.base_parser import BaseParser
from source.components.base_serializer import BaseSerializer
from source.components.base_writer import BaseWriter
from source.mvc.events.ui_event import UIEvent
from source.mvc.events.ui_event_type import UIEventType
from source.mvc.views.base_view import BaseView
from source.mvc.controllers.base_controller import BaseController
from source.config.config import Config


class PyUmlController(BaseController):
    def __init__(self,
                 view: BaseView,
                 writer: BaseWriter,
                 parser: BaseParser,
                 loader: BaseLoader,
                 serializer: BaseSerializer):
        self.__view = view
        self.__view.attach(self)
        self.__dot_writer = writer
        self.__class_parser = parser
        self.__serializer = serializer
        self.__loader = loader

        self.__ui_callbacks: dict = dict()
        self.register_ui_event()

    def run(self):
        self.__view.start()

    def update(self, event: UIEvent):
        event_type = event.get_type()
        event_body = event.get_body()
        if event_type in self.__ui_callbacks:
            self.__ui_callbacks[event_type](event_body)

    def register_ui_event(self):
        self.__ui_callbacks[UIEventType.UML] = self.py_uml
        self.__ui_callbacks[UIEventType.LOAD] = self.py_load
        self.__ui_callbacks[UIEventType.CONFIG] = self.py_config
        self.__ui_callbacks[UIEventType.VERSION] = self.py_version
        self.__ui_callbacks[UIEventType.EXIT] = self.py_exit

    def py_uml(self, event_body):
        input_path = event_body.input
        output_path = event_body.output
        print(input_path)
        code_string_list = \
            self.__loader.load_from_file_or_directory(input_path)

        for index, code_string in enumerate(code_string_list):
            dot_string = self.__parse_to_dot(code_string)
            self.__render_with_graphviz(output_path, index, dot_string)

    def py_load(self, event_body):
        pass

    def py_config(self, event_body):
        config = Config()
        content: str = "\nAuthor: " + config.author +\
                       "\nVersion: " + config.version +\
                       "\nUrl: " + config.url
        self.__view.view_print(content)

    def py_version(self, event_body):
        config = Config()
        content: str = "\nAra pyuml v" + config.version
        self.__view.view_print(content)

    def py_exit(self, event_body):
        self.__view.stop()

    def __parse_to_dot(self, code_string):
        """
        todo
        """
        class_parser = self.__parse_to_class_recoard(code_string)
        self.__persistent_to_file(class_parser.classes_list)
        dot_string = self.__dot_writer.write(class_parser.classes_list)
        return dot_string

    def __persistent_to_file(self, obj_list):
        assert obj_list is not None
        for obj in obj_list:
            self.__serializer.serialize(obj)

    def __parse_to_class_recoard(self, code_string):
        tree = ast3.parse(code_string)
        self.__class_parser.visit(tree)
        return self.__class_parser

    @staticmethod
    def __render_with_graphviz(output_path, index, dot):
        src = Source(dot)
        src.render(format='png',
                   filename='uml{}'.format(index),
                   directory=output_path)
