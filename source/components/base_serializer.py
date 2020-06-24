from abc import ABCMeta, abstractmethod


class BaseSerializer(metaclass=ABCMeta):
    @abstractmethod
    def serialize(self, obj):
        pass

    @abstractmethod
    def deserilize(self, name):
        pass

    @abstractmethod
    def get_keys(self):
        pass

    @abstractmethod
    def clear(self):
        pass
