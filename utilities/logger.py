import logging
import os
import sys


class Logger:
    """
    >>> obj1 = Logger()
    >>> obj2 = Logger() # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    AssertionError
    >>> obj3 = Logger.get_instance()
    >>> obj1 == obj3
    True
    """
    __instance = None

    @staticmethod
    def get_instance():
        """
        >>> obj1 = Logger.get_instance()
        >>> obj2 = Logger.get_instance()
        >>> obj1 == obj2
        True
        """
        if Logger.__instance is None:
            Logger()
        return Logger.__instance

    def __init__(self):
        assert Logger.__instance is None
        root_dir = os.path.dirname(sys.argv[0])
        self._path = os.path.join(root_dir, './log')
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
