import shelve

from core.parser import ClassRecorder


class Serializer:
    def __init__(self):
        pass

    def serialize(self, obj):
        assert isinstance(obj, ClassRecorder)
        with shelve.open('ast.db') as db:
            data = {"Members": len(obj.members), "Methods": len(obj.methods)}
            db[obj.name] = data
            print(obj.name)

    def deserilize(self, name):
        with shelve.open('ast.db') as db:
            data = db[name]

        return data


