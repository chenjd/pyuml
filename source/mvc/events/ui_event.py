from source.mvc.events.ui_event_type import UIEventType


class UIEvent:
    def __init__(self, event_type, body = None):
        self.__type: UIEventType = event_type
        self.__body = body

    def get_type(self):
        return self.__type

    def get_body(self):
        return self.__body
