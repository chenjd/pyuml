import inspect
import os
import sys
import unittest
from inspect import getsourcefile
from core.loader import Loader

TESTS_DIR = 'test_py_code'


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
        expected_files_count = 2
        self.assertEqual(expected_files_count, len(ret))

    def test_loader_load_from_directory_not_exist_throw_exception(self):
        local_dir = os.path.join(TESTS_DIR, "fake_folder")
        loader = Loader()
        with self.assertRaises(IOError):
            loader.load_from_file_or_directory(local_dir)


if __name__ == '__main__':
    test_dir = os.path.dirname(sys.argv[0])
    TESTS_DIR = os.path.join(test_dir, TESTS_DIR)
    unittest.main()
