from abc import ABCMeta, abstractmethod
from source.mvc.events.ui_event import UIEvent


# observer pattern
class BaseController(metaclass=ABCMeta):
    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def update(self, event: UIEvent):
        pass
