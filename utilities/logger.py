import logging
import os


class Logger:
    __instance = None

    @staticmethod
    def get_instance():
        if Logger.__instance is None:
            Logger()
        return Logger.__instance

    def __init__(self):
        assert Logger.__instance is None
        self._path = './log'
        self._logging = self._set_logging()
        Logger.__instance = self

    @property
    def logging(self):
        assert self._logging is not None
        return self._logging

    def _set_logging(self):
        if not os.path.exists(self._path):
            os.mkdir(self._path)

        logging.basicConfig(filename='./log/error.log', level=logging.DEBUG,
                            format='%(asctime)s %(levelname)s %(name)s %(message)s')
        return logging.getLogger(__name__)
