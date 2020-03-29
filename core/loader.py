import os


class Loader:

    def load_from_file_or_directory(self, path):
        """ (str) -> list of str
        Return list of str from one .py file of multiple .py files in a folder.

        >>> loader = Loader()
        >>> loader.load_from_file_or_directory('fake_path')
        Traceback (most recent call last):
        OSError
        """
        print(path)
        if not os.path.exists(path):
            raise IOError

        if os.path.isfile(path):
            return self._load_from_file(path)
        elif os.path.isdir(path):
            return self._load_from_directory(path)

    def _load_from_file(self, path):
        """
        >>> loader = Loader()
        >>> loader._load_from_file('test.px')
        Traceback (most recent call last):
        TypeError
        >>> loader._load_from_file('test.py')
        Could not load file:test.py
        """
        # path = '/Users/chenjiadong/Documents/funnyCode/PythonRepo/pyuml/OOPBasicClass.py'
        if not path.endswith('.py'):
            raise TypeError

        try:
            f = open(path, "r")
            string = f.read()
            f.close()
            assert isinstance(string, str)

            ret_string = list()
            ret_string.append(string)
            return ret_string

        except IOError:
            print("Could not load file:{}".format(path))

    def _load_from_directory(self, path):
        """
        >>> loader = Loader()
        >>> loader._load_from_directory('fake_path')
        Could not find:fake_path
        """
        assert path
        try:
            py_files = [os.path.join(path, fname) for fname in os.listdir(path) if fname.endswith('.py')]
            ret_string = list()
            for fname in py_files:
                f = open(fname, "r")
                string = f.read()
                f.close()
                ret_string.append(string)

            return ret_string

        except IOError:
            print("Could not find:{}".format(path))







