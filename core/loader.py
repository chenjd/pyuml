import os


class Loader:

    def load_from_file_or_directory(self, path):
        print(path)
        if not os.path.exists(path):
            raise IOError

        if os.path.isfile(path):
            return self._load_from_file(path)
        elif os.path.isdir(path):
            return self._load_from_directory(path)

    def _load_from_file(self, path):
        """
        :param path:
        :return:
        """
        # path = '/Users/chenjiadong/Documents/funnyCode/PythonRepo/pyuml/OOPBasicClass.py'
        if not path.endswith('.py'):
            raise TypeError

        try:
            f = open(path, "r")
            string = f.read()
            f.close()
            ret_string = list()
            ret_string.append(string)
            return ret_string

        except IOError:
            print("Could not load file:{}".format(path))

        except:
            pass

    def _load_from_directory(self, path):
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
            print("Could not load file:{}".format(fname))

        except:
            pass





