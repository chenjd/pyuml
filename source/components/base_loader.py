from abc import ABCMeta, abstractmethod


class BaseLoader(metaclass=ABCMeta):
    @abstractmethod
    def load_from_file_or_directory(self):
        pass
