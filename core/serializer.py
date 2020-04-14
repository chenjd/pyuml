import os
import shelve
import sys

from core.parser import ClassRecorder


class Serializer:
    """
    >>> import os
    >>> import pathlib
    >>> test_dir = pathlib.Path(__file__).parent.absolute()
    >>> folder = 'artifacts'
    >>> target_path = os.path.join(test_dir, folder)
    >>> obj = Serializer(target_path, 1)
    Traceback (most recent call last):
    AssertionError

    >>> obj = Serializer(target_path, 'path')
    >>> isinstance(obj, Serializer)
    True
    """
    def __init__(self, dir_path, file_name):
        assert isinstance(dir_path, str)
        assert isinstance(file_name, str)
        root_dir = os.path.dirname(sys.argv[0])
        self._folder_path = os.path.join(root_dir, dir_path)
        if not os.path.exists(self._folder_path):
            os.mkdir(self._folder_path)
        self._file_path = os.path.join(self._folder_path, file_name)

    def serialize(self, obj):
        """
        save the count of methods of a class and the count of date member of a class
        >>> import os
        >>> import pathlib
        >>> test_dir = pathlib.Path(__file__).parent.absolute()
        >>> folder = 'artifacts'
        >>> target_path = os.path.join(test_dir, folder)
        >>> obj = Serializer(target_path, 'path')
        >>> obj.serialize(1)
        Traceback (most recent call last):
        AssertionError

        >>> obj = Serializer(target_path, 'path')
        >>> target = ClassRecorder('test_name', list())
        >>> obj.serialize(target)
        test_name
        """
        assert isinstance(obj, ClassRecorder)
        with shelve.open(self._file_path) as db:
            data = {"Members": len(obj.members), "Methods": len(obj.methods)}
            db[obj.name] = data
            print(obj.name)

    def deserilize(self, name):
        """
        >>> import os
        >>> import pathlib
        >>> test_dir = pathlib.Path(__file__).parent.absolute()
        >>> folder = 'artifacts'
        >>> target_path = os.path.join(test_dir, folder)
        >>> obj = Serializer(target_path, 'path')
        >>> obj.deserilize(1)
        Traceback (most recent call last):
        AssertionError
        """
        assert isinstance(name, str)
        with shelve.open(self._file_path) as db:
            data = db[name]

        return data

    def get_keys(self):
        with shelve.open(self._file_path) as db:
            klist = list(db.keys())
        return klist

    def clear(self):
        with shelve.open(self._file_path) as db:
            db.clear()



