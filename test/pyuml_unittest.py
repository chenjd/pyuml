import inspect
import os
import sys
import unittest

from typed_ast import ast3

from core.loader import Loader
from core.parser import ClassParser
from core.writer import DotWriter

TESTS_DIR = 'test_py_code'
TESTS_DIR2 = 'test_dot_code'


class TestPyUmlAPI(unittest.TestCase):

    def test_loader_load_from_file_success(self):
        local_dir = os.path.join(TESTS_DIR, "py_src_code_hello_world.py")
        loader = Loader()
        loaded_code = loader.load_from_file_or_directory(local_dir)
        expected_code = """class MyClass:\n    i = 12345\n"""
        self.assertMultiLineEqual(expected_code, loaded_code[0])

    def test_loader_load_from_file_not_exist_throw_exception(self):
        local_dir = os.path.join(TESTS_DIR, "py_src_code_hello_.py")
        loader = Loader()
        with self.assertRaises(IOError):
            loader.load_from_file_or_directory(local_dir)

    def test_loader_load_from_file_file_type_wrong_throw_exception(self):
        local_dir = os.path.join(TESTS_DIR, "py_src_code_hello_world.py1")
        loader = Loader()
        with self.assertRaises(TypeError):
            loader.load_from_file_or_directory(local_dir)

    def test_loader_load_from_directory_find_out_py_file(self):
        loader = Loader()
        ret = loader.load_from_file_or_directory(TESTS_DIR)
        expected_files_count = 8
        self.assertEqual(expected_files_count, len(ret))

    def test_loader_load_from_directory_not_exist_throw_exception(self):
        local_dir = os.path.join(TESTS_DIR, "fake_folder")
        loader = Loader()
        with self.assertRaises(IOError):
            loader.load_from_file_or_directory(local_dir)

    def test_parser_parse_only_class_define(self):
        local_dir = os.path.join(TESTS_DIR, "py_src_code_only_class_def.py")
        loader = Loader()
        code_string_list = loader.load_from_file_or_directory(local_dir)
        tree = ast3.parse(code_string_list[0])
        class_parser = ClassParser()
        class_parser.visit(tree)

        expected_class_name = "MyClass"
        expected_memober_count = 0
        self.assertEqual(expected_class_name, class_parser.classes_list[0].name)
        self.assertEqual(expected_memober_count, len(class_parser.classes_list[0].members))
        self.assertEqual(expected_memober_count, len(class_parser.classes_list[0].methods))

    def test_parser_parse_class_with_constructor(self):
        local_dir = os.path.join(TESTS_DIR, "py_src_code_class_with_constructor.py")
        loader = Loader()
        code_string_list = loader.load_from_file_or_directory(local_dir)
        tree = ast3.parse(code_string_list[0])
        class_parser = ClassParser()
        class_parser.visit(tree)

        expected_class_name = "MyClass"
        expected_memober_count = 0
        expected_methods_count = 1
        self.assertEqual(expected_class_name, class_parser.classes_list[0].name)
        self.assertEqual(expected_memober_count, len(class_parser.classes_list[0].members))
        self.assertEqual(expected_methods_count, len(class_parser.classes_list[0].methods))

    def test_parser_parse_class_with_constructor_data_members(self):
        local_dir = os.path.join(TESTS_DIR, "py_src_code_class_with_data.py")
        loader = Loader()
        code_string_list = loader.load_from_file_or_directory(local_dir)
        tree = ast3.parse(code_string_list[0])
        class_parser = ClassParser()
        class_parser.visit(tree)

        expected_class_name = "MyClass"
        expected_memober_count = 5
        expected_methods_count = 1
        self.assertEqual(expected_class_name, class_parser.classes_list[0].name)
        self.assertEqual(expected_memober_count, len(class_parser.classes_list[0].members))
        self.assertEqual(expected_methods_count, len(class_parser.classes_list[0].methods))

    def test_parser_parse_class_with_constructor_data_members_methods(self):
        local_dir = os.path.join(TESTS_DIR, "py_src_code_class_with_data_methods.py")
        loader = Loader()
        code_string_list = loader.load_from_file_or_directory(local_dir)
        tree = ast3.parse(code_string_list[0])
        class_parser = ClassParser()
        class_parser.visit(tree)

        expected_class_name = "MyClass"
        expected_memober_count = 5
        expected_methods_count = 3
        self.assertEqual(expected_class_name, class_parser.classes_list[0].name)
        self.assertEqual(expected_memober_count, len(class_parser.classes_list[0].members))
        self.assertEqual(expected_methods_count, len(class_parser.classes_list[0].methods))

    def test_parser_parse_classes_inheritance(self):
        local_dir = os.path.join(TESTS_DIR, "py_src_code_classes_inheritance.py")
        loader = Loader()
        code_string_list = loader.load_from_file_or_directory(local_dir)
        tree = ast3.parse(code_string_list[0])
        class_parser = ClassParser()
        class_parser.visit(tree)

        for cla in class_parser.classes_list:
            if cla.name is "BaseClass":
                self.assertEqual(0, len(cla.parents))
            elif cla.name is "MyClassOne":
                self.assertEqual(1, len(cla.parents))
            elif cla.name is "MyClassTwo":
                self.assertEqual(2, len(cla.parents))

    def test_writter_write_dot_only_class_define(self):
        local_dir = os.path.join(TESTS_DIR, "py_src_code_only_class_def.py")
        loader = Loader()
        code_string_list = loader.load_from_file_or_directory(local_dir)
        tree = ast3.parse(code_string_list[0])
        class_parser = ClassParser()
        class_parser.visit(tree)

        writer = DotWriter()
        result_dot = writer.write(class_parser.classes_list)

        dot_path = os.path.join(TESTS_DIR2, "uml0")
        with open(dot_path, 'r') as f:
            expected_dot = f.read()

        self.assertMultiLineEqual(expected_dot, result_dot)

    def test_writter_write_dot_class_with_constructor(self):
        local_dir = os.path.join(TESTS_DIR, "py_src_code_class_with_constructor.py")
        loader = Loader()
        code_string_list = loader.load_from_file_or_directory(local_dir)
        tree = ast3.parse(code_string_list[0])
        class_parser = ClassParser()
        class_parser.visit(tree)

        writer = DotWriter()
        result_dot = writer.write(class_parser.classes_list)

        dot_path = os.path.join(TESTS_DIR2, "uml2")
        with open(dot_path, 'r') as f:
            expected_dot = f.read()

        self.assertMultiLineEqual(expected_dot, result_dot)

    def test_writter_write_dot_class_with_constructor_data_members(self):
        local_dir = os.path.join(TESTS_DIR, "py_src_code_class_with_data.py")
        loader = Loader()
        code_string_list = loader.load_from_file_or_directory(local_dir)
        tree = ast3.parse(code_string_list[0])
        class_parser = ClassParser()
        class_parser.visit(tree)

        writer = DotWriter()
        result_dot = writer.write(class_parser.classes_list)

        dot_path = os.path.join(TESTS_DIR2, "uml5")
        with open(dot_path, 'r') as f:
            expected_dot = f.read()

        self.assertMultiLineEqual(expected_dot, result_dot)

    def test_writter_write_dot_class_with_constructor_data_members_methods(self):
        local_dir = os.path.join(TESTS_DIR, "py_src_code_class_with_data_methods.py")
        loader = Loader()
        code_string_list = loader.load_from_file_or_directory(local_dir)
        tree = ast3.parse(code_string_list[0])
        class_parser = ClassParser()
        class_parser.visit(tree)

        writer = DotWriter()
        result_dot = writer.write(class_parser.classes_list)

        dot_path = os.path.join(TESTS_DIR2, "uml1")
        with open(dot_path, 'r') as f:
            expected_dot = f.read()

        self.assertMultiLineEqual(expected_dot, result_dot)

    def test_writter_write_dot_class_classes_inheritance(self):
        local_dir = os.path.join(TESTS_DIR, "py_src_code_classes_inheritance.py")
        loader = Loader()
        code_string_list = loader.load_from_file_or_directory(local_dir)
        tree = ast3.parse(code_string_list[0])
        class_parser = ClassParser()
        class_parser.visit(tree)

        writer = DotWriter()
        result_dot = writer.write(class_parser.classes_list)

        dot_path = os.path.join(TESTS_DIR2, "uml3")
        with open(dot_path, 'r') as f:
            expected_dot = f.read()

        self.assertMultiLineEqual(expected_dot, result_dot)

    def test_pyuml_source_code_syntax_error(self):
        local_dir = os.path.join(TESTS_DIR, "py_src_code_error.py")
        loader = Loader()
        code_string_list = loader.load_from_file_or_directory(local_dir)
        with self.assertRaises(SyntaxError):
            tree = ast3.parse(code_string_list[0])


if __name__ == '__main__':
    test_dir = os.path.dirname(sys.argv[0])
    TESTS_DIR = os.path.join(test_dir, TESTS_DIR)
    TESTS_DIR2 = os.path.join(test_dir, TESTS_DIR2)
    unittest.main()
