
class Loader:

    def load_from_file(self, path):
        """
        :param path:
        :return:
        """
        path = '/Users/chenjiadong/Documents/funnyCode/PythonRepo/pyuml/OOPBasicClass.py'
        f = open(path, "r")
        string = f.read()
        print(string)
        f.close()
        return string

