from abc import ABCMeta, abstractmethod


class BaseWriter(metaclass=ABCMeta):
    @abstractmethod
    def write(self, classes):
        pass
