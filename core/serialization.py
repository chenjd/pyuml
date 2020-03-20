import shelve


class Serialization:
    def __init__(self):
        pass

    def write(self, obj):
        db = shelve.open("ast.db")
        db.dict["test"] = 1

