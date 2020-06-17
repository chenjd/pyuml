from abc import ABCMeta, abstractmethod
from source.mvc.events.ui_event import UIEvent


# Subject
class BaseView(metaclass=ABCMeta):
    def __init__(self):
        self.__observers: list = []

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def view_print(self):
        pass

    def attach(self, observer):
        self.__observers.append(observer)

    def detach(self, observer):
        self.__observers.remove(observer)

    def notify(self, event: UIEvent):
        for o in self.__observers:
            o.update(event)


