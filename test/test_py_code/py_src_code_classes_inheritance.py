class BaseClass:
    def __init__(self):
        pass

    @staticmethod
    def say_hi():
        print("hi")


class MyClassOne(BaseClass):
    def __init__(self):
        pass


class MyClassTwo(BaseClass, MyClassOne):
    def __init__(self):
        pass
