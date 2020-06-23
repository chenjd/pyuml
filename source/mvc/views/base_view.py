from abc import ABCMeta, abstractmethod

from source.mvc.controllers.base_controller import BaseController
from source.mvc.events.ui_event import UIEvent
from typing import List


class BaseView(metaclass=ABCMeta):
    def __init__(self):
        self.__observers: List[BaseController] = []

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


