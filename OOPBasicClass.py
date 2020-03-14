# Code from https://github.com/hussien89aa/PythonTutorial
class Goods:
    def __init__(self):
        pass


class Car(Goods):
    def __init__(self):
        self.num_one = 1
        self.num_two = 2;
        self._Name = "private"

    def GetOwner(self):
        print("Owner is ", self._Name)

    def SetOwner(self, Name):
        self._Name = Name


def main():
    mycar = Car()
    mycar.SetOwner("Hussein Alrubaye")
    mycar.GetOwner()
    Jencar = Car()
    Jencar.SetOwner("Jen Alrubaye")
    Jencar.GetOwner()


if __name__ == '__main__': main()
