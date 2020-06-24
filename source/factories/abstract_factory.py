from abc import ABCMeta, abstractmethod


class AbstractFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_view(self):
        pass

    @abstractmethod
    def create_controller(self, view):
        pass
