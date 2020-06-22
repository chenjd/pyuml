import os
from source.components.base_loader import BaseLoader


class PythonFilesLoader(BaseLoader):

    def load_from_file_or_directory(self, path):
        """ (str) -> list of str
        Return list of str from one .py file of multiple .py files in a folder.

        >>> loader = PythonFilesLoader()
        >>> loader.load_from_file_or_directory('fake_path')
        Traceback (most recent call last):
        OSError
        """
        print(path)
        if not os.path.exists(path):
            raise IOError

        if os.path.isfile(path):
            return self._load_from_file(path)
        else:
            return self._load_from_directory(path)

    @staticmethod
    def _load_from_file(path):
        """
        >>> loader = PythonFilesLoader()
        >>> loader._load_from_file('test.px')
        Traceback (most recent call last):
        TypeError
        >>> loader._load_from_file('test.py')
        Could not load file:test.py
        """
        if not path.endswith('.py'):
            raise TypeError

        f = open(path, "r")
        string = f.read()
        f.close()
        assert isinstance(string, str)

        ret_string = list()
        ret_string.append(string)
        return ret_string

    @staticmethod
    def _load_from_directory(path):
        """
        >>> loader = PythonFilesLoader()
        >>> loader._load_from_directory('fake_path')
        Could not find:fake_path
        """
        assert path
        py_files = [os.path.join(path, fname) for fname in os.listdir(path)
                    if fname.endswith('.py')]
        ret_string = list()
        for fname in py_files:
            f = open(fname, "r")
            string = f.read()
            f.close()
            ret_string.append(string)

        return ret_string







