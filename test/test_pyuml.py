import os
import unittest
import contextlib
from io import StringIO
from PIL import Image
import imagehash
from typed_ast import ast3
import pathlib

from source.components.python_files_loader import PythonFilesLoader
from source.components.python_parser import PythonParser
from source.components.shelve_serializer import ShelveSerializer
from source.components.dot_writer import DotWriter
from source.config.config import Config
from source.factories.cmd_python_uml_factory import CmdPythonUmlFactory
from source.mvc.models.class_recorder import ClassRecorder


class TestPyUmlAPI(unittest.TestCase):

    def setUp(self) -> None:
        test_py_dir = 'test_py_code'
        test_dot_dir = 'test_dot_code'
        test_db_dir = 'test_db'
        test_artifacts_dir = 'test_artifacts'
        test_dir = pathlib.Path(__file__).parent.absolute()
        self.test_py_dir = os.path.join(test_dir, test_py_dir)
        self.test_dot_dir = os.path.join(test_dir, test_dot_dir)
        self.test_db_dir = os.path.join(test_dir, test_db_dir)
        self.test_artifacts_dir = os.path.join(test_dir, test_artifacts_dir)

    def test_loader_load_from_file_success(self):
        local_dir = os.path.join(self.test_py_dir,
                                 "py_src_code_hello_world.py")
        loader = PythonFilesLoader()
        loaded_code = loader.load_from_file_or_directory(local_dir)
        expected_code = """class MyClass:\n    i = 12345\n"""
        self.assertMultiLineEqual(expected_code, loaded_code[0])

    def test_loader_load_from_directory_success(self):
        local_dir = self.test_py_dir
        expected_result = 12
        loader = PythonFilesLoader()
        loaded_code_list = loader.load_from_file_or_directory(local_dir)
        self.assertEqual(len(loaded_code_list), expected_result)

    def test_loader_load_from_file_not_exist_throw_exception(self):
        local_dir = os.path.join(self.test_py_dir, "py_src_code_hello_.py")
        loader = PythonFilesLoader()
        with self.assertRaises(IOError):
            loader.load_from_file_or_directory(local_dir)

    def test_loader_load_from_file_file_type_wrong_throw_exception(self):
        local_dir = os.path.join(self.test_py_dir,
                                 "py_src_code_hello_world.py1")
        loader = PythonFilesLoader()
        with self.assertRaises(TypeError):
            loader.load_from_file_or_directory(local_dir)

    def test_loader_load_from_directory_find_out_py_file(self):
        loader = PythonFilesLoader()
        ret = loader.load_from_file_or_directory(self.test_py_dir)
        expected_files_count = 12
        self.assertEqual(expected_files_count, len(ret))

    def test_loader_load_from_directory_not_exist_throw_exception(self):
        local_dir = os.path.join(self.test_py_dir, "fake_folder")
        loader = PythonFilesLoader()
        with self.assertRaises(IOError):
            loader.load_from_file_or_directory(local_dir)

    def test_parser_parse_only_class_define(self):
        local_dir = os.path.join(self.test_py_dir,
                                 "py_src_code_only_class_def.py")
        loader = PythonFilesLoader()
        code_string_list = loader.load_from_file_or_directory(local_dir)
        tree = ast3.parse(code_string_list[0])
        class_parser = PythonParser(ClassRecorder)
        class_parser.visit(tree)

        expected_class_name = "MyClass"
        expected_memober_count = 0
        self.assertEqual(expected_class_name,
                         class_parser.classes_list[0].name)
        self.assertEqual(expected_memober_count,
                         len(class_parser.classes_list[0].members))
        self.assertEqual(expected_memober_count,
                         len(class_parser.classes_list[0].methods))

    def test_parser_parse_class_with_constructor(self):
        local_dir = os.path.join(self.test_py_dir,
                                 "py_src_code_class_with_constructor.py")
        loader = PythonFilesLoader()
        code_string_list = loader.load_from_file_or_directory(local_dir)
        tree = ast3.parse(code_string_list[0])
        class_parser = PythonParser(ClassRecorder)
        class_parser.visit(tree)

        expected_class_name = "MyClass"
        expected_memober_count = 0
        expected_methods_count = 1
        self.assertEqual(expected_class_name,
                         class_parser.classes_list[0].name)
        self.assertEqual(expected_memober_count,
                         len(class_parser.classes_list[0].members))
        self.assertEqual(expected_methods_count,
                         len(class_parser.classes_list[0].methods))

    def test_parser_parse_class_with_constructor_data_members_type(self):
        local_dir = os.path.join(self.test_py_dir,
                                 "py_src_code_class_with_data_type.py")
        loader = PythonFilesLoader()
        code_string_list = loader.load_from_file_or_directory(local_dir)
        tree = ast3.parse(code_string_list[0])
        class_parser = PythonParser(ClassRecorder)
        class_parser.visit(tree)

        expected_class_name = "MyClass"
        expected_memober_count = 4
        expected_methods_count = 1
        self.assertEqual(expected_class_name,
                         class_parser.classes_list[0].name)
        self.assertEqual(expected_memober_count,
                         len(class_parser.classes_list[0].members))
        self.assertEqual(expected_methods_count,
                         len(class_parser.classes_list[0].methods))

    def test_parser_parse_class_with_constructor_data_members(self):
        local_dir = os.path.join(self.test_py_dir,
                                 "py_src_code_class_with_data.py")
        loader = PythonFilesLoader()
        code_string_list = loader.load_from_file_or_directory(local_dir)
        tree = ast3.parse(code_string_list[0])
        class_parser = PythonParser(ClassRecorder)
        class_parser.visit(tree)

        expected_class_name = "MyClass"
        expected_memober_count = 5
        expected_methods_count = 1
        self.assertEqual(expected_class_name,
                         class_parser.classes_list[0].name)
        self.assertEqual(expected_memober_count,
                         len(class_parser.classes_list[0].members))
        self.assertEqual(expected_methods_count,
                         len(class_parser.classes_list[0].methods))

    def test_parser_parse_class_with_constructor_data_members_methods(self):
        local_dir = os.path.join(self.test_py_dir,
                                 "py_src_code_class_with_data_methods.py")
        loader = PythonFilesLoader()
        code_string_list = loader.load_from_file_or_directory(local_dir)
        tree = ast3.parse(code_string_list[0])
        class_parser = PythonParser(ClassRecorder)
        class_parser.visit(tree)

        expected_class_name = "MyClass"
        expected_memober_count = 5
        expected_methods_count = 3
        self.assertEqual(expected_class_name,
                         class_parser.classes_list[0].name)
        self.assertEqual(expected_memober_count,
                         len(class_parser.classes_list[0].members))
        self.assertEqual(expected_methods_count,
                         len(class_parser.classes_list[0].methods))

    def test_parser_parse_class_with_constructor_private_data_members(self):
        local_dir = os.path.join(self.test_py_dir,
                                 "py_src_code_class_with_private_data.py")
        loader = PythonFilesLoader()
        code_string_list = loader.load_from_file_or_directory(local_dir)
        tree = ast3.parse(code_string_list[0])
        class_parser = PythonParser(ClassRecorder)
        class_parser.visit(tree)

        expected_class_name = "MyClass"
        expected_memober_count = 5
        expected_methods_count = 3
        self.assertEqual(expected_class_name,
                         class_parser.classes_list[0].name)
        self.assertEqual(expected_memober_count,
                         len(class_parser.classes_list[0].members))
        self.assertEqual(expected_methods_count,
                         len(class_parser.classes_list[0].methods))

    def test_parser_parse_class_with_argument_methods(self):
        local_dir = os.path.join(self.test_py_dir,
                                 "py_src_code_class_argument_method.py")
        loader = PythonFilesLoader()
        code_string_list = loader.load_from_file_or_directory(local_dir)
        tree = ast3.parse(code_string_list[0])
        class_parser = PythonParser(ClassRecorder)
        class_parser.visit(tree)

        expected_class_name = "MyClass"
        expected_memober_count = 5
        expected_methods_count = 5
        self.assertEqual(expected_class_name,
                         class_parser.classes_list[0].name)
        self.assertEqual(expected_memober_count,
                         len(class_parser.classes_list[0].members))
        self.assertEqual(expected_methods_count,
                         len(class_parser.classes_list[0].methods))

    def test_parser_parse_classes_inheritance(self):
        local_dir = os.path.join(self.test_py_dir,
                                 "py_src_code_classes_inheritance.py")
        loader = PythonFilesLoader()
        code_string_list = loader.load_from_file_or_directory(local_dir)
        tree = ast3.parse(code_string_list[0])
        class_parser = PythonParser(ClassRecorder)
        class_parser.visit(tree)

        for cla in class_parser.classes_list:
            if cla.name is "BaseClass":
                self.assertEqual(0, len(cla.parents))
            elif cla.name is "MyClassOne":
                self.assertEqual(1, len(cla.parents))
            elif cla.name is "MyClassTwo":
                self.assertEqual(2, len(cla.parents))

    def test_writter_write_dot_only_class_define(self):
        local_dir = os.path.join(self.test_py_dir,
                                 "py_src_code_only_class_def.py")
        loader = PythonFilesLoader()
        code_string_list = loader.load_from_file_or_directory(local_dir)
        tree = ast3.parse(code_string_list[0])
        class_parser = PythonParser(ClassRecorder)
        class_parser.visit(tree)

        writer = DotWriter()
        result_dot = writer.write(class_parser.classes_list)

        dot_path = os.path.join(self.test_dot_dir, "uml0")
        with open(dot_path, 'r') as f:
            expected_dot = f.read()

        self.assertMultiLineEqual(expected_dot, result_dot)

    def test_writter_write_dot_class_with_constructor(self):
        local_dir = os.path.join(self.test_py_dir,
                                 "py_src_code_class_with_constructor.py")
        loader = PythonFilesLoader()
        code_string_list = loader.load_from_file_or_directory(local_dir)
        tree = ast3.parse(code_string_list[0])
        class_parser = PythonParser(ClassRecorder)
        class_parser.visit(tree)

        writer = DotWriter()
        result_dot = writer.write(class_parser.classes_list)

        dot_path = os.path.join(self.test_dot_dir, "uml3")
        with open(dot_path, 'r') as f:
            expected_dot = f.read()

        self.assertMultiLineEqual(expected_dot, result_dot)

    def test_writter_write_dot_class_with_constructor_data_members(self):
        local_dir = os.path.join(self.test_py_dir,
                                 "py_src_code_class_with_data.py")
        loader = PythonFilesLoader()
        code_string_list = loader.load_from_file_or_directory(local_dir)
        tree = ast3.parse(code_string_list[0])
        class_parser = PythonParser(ClassRecorder)
        class_parser.visit(tree)

        writer = DotWriter()
        result_dot = writer.write(class_parser.classes_list)

        dot_path = os.path.join(self.test_dot_dir, "uml7")
        with open(dot_path, 'r') as f:
            expected_dot = f.read()

        self.assertMultiLineEqual(expected_dot, result_dot)

    def test_writer_write_dot_class_constructor_data_members_methods(self):
        local_dir = os.path.join(self.test_py_dir,
                                 "py_src_code_class_with_data_methods.py")
        loader = PythonFilesLoader()
        code_string_list = loader.load_from_file_or_directory(local_dir)
        tree = ast3.parse(code_string_list[0])
        class_parser = PythonParser(ClassRecorder)
        class_parser.visit(tree)

        writer = DotWriter()
        result_dot = writer.write(class_parser.classes_list)

        dot_path = os.path.join(self.test_dot_dir, "uml2")
        with open(dot_path, 'r') as f:
            expected_dot = f.read()

        self.assertMultiLineEqual(expected_dot, result_dot)

    def test_writter_write_dot_class_classes_inheritance(self):
        local_dir = os.path.join(self.test_py_dir,
                                 "py_src_code_classes_inheritance.py")
        loader = PythonFilesLoader()
        code_string_list = loader.load_from_file_or_directory(local_dir)
        tree = ast3.parse(code_string_list[0])
        class_parser = PythonParser(ClassRecorder)
        class_parser.visit(tree)

        writer = DotWriter()
        result_dot = writer.write(class_parser.classes_list)

        dot_path = os.path.join(self.test_dot_dir, "uml5")
        with open(dot_path, 'r') as f:
            expected_dot = f.read()

        self.assertMultiLineEqual(expected_dot, result_dot)

    def test_pyuml_source_code_syntax_error(self):
        local_dir = os.path.join(self.test_py_dir, "py_src_code_error.py")
        loader = PythonFilesLoader()
        code_string_list = loader.load_from_file_or_directory(local_dir)
        with self.assertRaises(SyntaxError):
            ast3.parse(code_string_list[0])

    def test_serializer_serialize_save_classname_as_key(self):
        local_dir = os.path.join(self.test_py_dir,
                                 "py_src_code_class_with_data_methods.py")
        target_file = "ast_test.db"
        loader = PythonFilesLoader()
        code_string_list = loader.load_from_file_or_directory(local_dir)
        tree = ast3.parse(code_string_list[0])
        class_parser = PythonParser(ClassRecorder)
        class_parser.visit(tree)
        serializer = ShelveSerializer(self.test_db_dir, target_file)
        serializer.clear()
        serializer.serialize(class_parser.classes_list[0])
        self.assertEqual(serializer.get_keys()[0], "MyClass")

    def test_serializer_serialize_save_multiple_class_data(self):
        local_dir = os.path.join(self.test_py_dir,
                                 "py_src_code_classes_inheritance.py")
        target_file = "ast_test.db"
        loader = PythonFilesLoader()
        code_string_list = loader.load_from_file_or_directory(local_dir)
        tree = ast3.parse(code_string_list[0])
        class_parser = PythonParser(ClassRecorder)
        class_parser.visit(tree)
        serializer = ShelveSerializer(self.test_db_dir, target_file)
        serializer.clear()
        for cls in class_parser.classes_list:
            serializer.serialize(cls)

        expected_class_count = 3
        self.assertEqual(expected_class_count, len(serializer.get_keys()))

    def test_serializer_deserialize_file_do_not_exist(self):
        local_dir = os.path.join(self.test_py_dir,
                                 "py_src_code_class_with_data.py")
        target_file = "fake_test.db"
        loader = PythonFilesLoader()
        code_string_list = loader.load_from_file_or_directory(local_dir)
        tree = ast3.parse(code_string_list[0])
        class_parser = PythonParser(ClassRecorder)
        class_parser.visit(tree)
        serializer = ShelveSerializer(self.test_db_dir, target_file)
        with self.assertRaises(KeyError):
            serializer.deserilize('Test')

    def test_serializer_deserialize_key_do_not_exist(self):
        local_dir = os.path.join(self.test_py_dir,
                                 "py_src_code_class_with_data.py")
        target_file = "ast_test.db"
        loader = PythonFilesLoader()
        code_string_list = loader.load_from_file_or_directory(local_dir)
        tree = ast3.parse(code_string_list[0])
        class_parser = PythonParser(ClassRecorder)
        class_parser.visit(tree)
        serializer = ShelveSerializer(self.test_db_dir, target_file)
        serializer.clear()
        for cls in class_parser.classes_list:
            serializer.serialize(cls)
        with self.assertRaises(KeyError):
            serializer.deserilize('Test')

    def test_serializer_deserialize_member_count(self):
        local_dir = os.path.join(self.test_py_dir,
                                 "py_src_code_class_with_data.py")
        target_file = "ast_test.db"
        loader = PythonFilesLoader()
        code_string_list = loader.load_from_file_or_directory(local_dir)
        tree = ast3.parse(code_string_list[0])
        class_parser = PythonParser(ClassRecorder)
        class_parser.visit(tree)
        serializer = ShelveSerializer(self.test_db_dir, target_file)
        serializer.clear()
        for cls in class_parser.classes_list:
            serializer.serialize(cls)
        cls_data = serializer.deserilize('MyClass')
        expected_m_count = 5
        self.assertEqual(expected_m_count, cls_data['Members'])

    def test_serializer_deserialize_method_count(self):
        local_dir = os.path.join(self.test_py_dir,
                                 "py_src_code_class_with_data_methods.py")
        target_file = "ast_test.db"
        loader = PythonFilesLoader()
        code_string_list = loader.load_from_file_or_directory(local_dir)
        tree = ast3.parse(code_string_list[0])
        class_parser = PythonParser(ClassRecorder)
        class_parser.visit(tree)
        serializer = ShelveSerializer(self.test_db_dir, target_file)
        serializer.clear()
        for cls in class_parser.classes_list:
            serializer.serialize(cls)
        cls_data = serializer.deserilize('MyClass')
        expected_m_count = 3
        self.assertEqual(expected_m_count, cls_data['Methods'])

    def test_parser_type_comments_type_annotation_result_same(self):
        py_annotation_path = os.path.join(self.test_py_dir,
                                          "py_type_annotations.py")
        py_comments_path = os.path.join(self.test_py_dir,
                                        "py_type_comments.py")
        loader = PythonFilesLoader()
        py_annotation_code = loader. \
            load_from_file_or_directory(py_annotation_path)
        py_comments_code = loader.load_from_file_or_directory(py_comments_path)

        py_annotation_tree = ast3.parse(py_annotation_code[0])
        py_comments_tree = ast3.parse(py_comments_code[0])

        class_parser = PythonParser(ClassRecorder)
        class_parser.visit(py_annotation_tree)
        writer = DotWriter()
        py_annotation_dot = writer.write(class_parser.classes_list)

        class_parser.clear()
        class_parser.visit(py_comments_tree)
        py_comments_dot = writer.write(class_parser.classes_list)
        self.assertEqual(py_annotation_dot, py_comments_dot)

    def test_view_do_version(self):
        pyuml = self.create_view_and_controller()
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            pyuml.do_version(None)
        output = temp_stdout.getvalue().strip()
        config = Config()
        self.assertEqual(output,
                         "cmd_view: " + "\nAra pyuml v" + config.version)

    def test_view_do_config(self):
        pyuml = self.create_view_and_controller()
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            pyuml.do_config(None)
        output = temp_stdout.getvalue().strip()
        config = Config()
        self.assertEqual(output, "cmd_view: " + "\nAuthor: " +
                         config.author + "\nVersion: "
                         + config.version + "\nUrl: " + config.url)

    def test_view_do_exit(self):
        pyuml = self.create_view_and_controller()
        with self.assertRaises(SystemExit):
            pyuml.do_exit(None)

    def test_view_do_uml_generate_uml(self):
        pyuml = self.create_view_and_controller()
        input_dir = os.path.join(self.test_py_dir,
                                 "py_src_code_only_class_def.py")
        output_dir = self.test_artifacts_dir
        pyuml.do_2uml(input_dir + ' ' + output_dir)
        expected_img_path = os.path.join(self.test_dot_dir, "uml0.png")
        expected_hash = imagehash.average_hash(Image.open(expected_img_path))
        result_img_path = os.path.join(self.test_artifacts_dir, "uml0.png")
        result_hash = imagehash.average_hash(Image.open(result_img_path))

        self.assertEqual(expected_hash, result_hash)

    def test_view_do_uml_wrong_arguments(self):
        pyuml = self.create_view_and_controller()
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            pyuml.do_2uml('e e')
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, "e\nException: Check the error log")

    def test_view_do_load_load_data(self):
        pyuml = self.create_view_and_controller()
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            pyuml.do_load('MyClass')
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, "{'Members': 0, 'Methods': 0}")

    def test_view_do_load_without_key(self):
        pyuml = self.create_view_and_controller()
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            pyuml.do_load('missing')
        output = temp_stdout.getvalue().strip()
        print(output)
        self.assertEqual(output, "Exception: Check the error log")

    @staticmethod
    def create_view_and_controller():
        factory = CmdPythonUmlFactory()
        view = factory.create_view()
        factory.create_controller(view)
        return view


if __name__ == '__main__':
    unittest.main()
