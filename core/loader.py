
class Loader:

    def load_from_file(self, path):
        """
        :param path:
        :return:
        """
        # path = '/Users/chenjiadong/Documents/funnyCode/PythonRepo/pyuml/OOPBasicClass.py'
        try:
            f = open(path, "r")
            string = f.read()
            print(string)
            f.close()
            return string

        except IOError:
            print("Could not load file:{}".format(path))

        except:
            pass


