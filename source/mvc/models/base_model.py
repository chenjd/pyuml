from abc import ABCMeta, abstractmethod


class BaseModel(metaclass=ABCMeta):
    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def load(self, key):
        pass
