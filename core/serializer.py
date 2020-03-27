import shelve

from core.parser import ClassRecorder


class Serializer:
    def __init__(self, path):
        assert isinstance(path, str)
        self._path = path

    def serialize(self, obj):
        assert isinstance(obj, ClassRecorder)
        with shelve.open(self._path) as db:
            data = {"Members": len(obj.members), "Methods": len(obj.methods)}
            db[obj.name] = data
            print(obj.name)

    def deserilize(self, name):
        assert isinstance(name, str)
        with shelve.open(self._path) as db:
            data = db[name]

        return data

    def get_keys(self):
        with shelve.open(self._path) as db:
            klist = list(db.keys())
        return klist

    def clear(self):
        with shelve.open(self._path) as db:
            db.clear()



