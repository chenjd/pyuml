import logging
import os
import sys


class Logger:
    """
    >>> obj1 = Logger(True)
    >>> obj2 = Logger(True) # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    AssertionError
    >>> obj3 = Logger.get_instance(True)
    >>> obj1 == obj3
    True
    """
    __instance = None

    @staticmethod
    def get_instance(is_doctest=False):
        """
        >>> obj1 = Logger.get_instance(True)
        >>> obj2 = Logger.get_instance(True)
        >>> obj1 == obj2
        True
        """
        if Logger.__instance is None:
            Logger(is_doctest)
        return Logger.__instance

    def __init__(self, is_doctest=False):
        assert Logger.__instance is None
        root_dir = os.path.dirname(sys.argv[0])
        if is_doctest:
            import pathlib
            root_dir = os.path.dirname(pathlib.Path(__file__).parent.absolute())

        self._path = os.path.join(root_dir, 'log')
        self._logging = self._set_logging()
        Logger.__instance = self

    @property
    def logging(self):
        assert self._logging is not None
        return self._logging

    def _set_logging(self):
        if not os.path.exists(self._path):
            os.mkdir(self._path)

        logging.basicConfig(filename=os.path.join(self._path, 'error.log'), level=logging.DEBUG,
                            format='%(asctime)s %(levelname)s %(name)s %(message)s')
        return logging.getLogger(__name__)
