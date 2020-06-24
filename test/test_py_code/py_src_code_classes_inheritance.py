class BaseClass:
    def __init__(self):
        pass

    def say_hi(self):
        print("hi")


class MyClassOne(BaseClass):
    def __init__(self):
        pass


class MyClassTwo(BaseClass, MyClassOne):
    def __init__(self):
        pass
