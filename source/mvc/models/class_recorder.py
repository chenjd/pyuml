from source.mvc.models.base_model import BaseModel


class ClassRecorder(BaseModel):
    def __init__(self, name, parents, serializer = None):
        self._name = name
        self._members = list()
        self._methods = list()
        self._base_classes = parents
        self._serialize = serializer

    def save(self):
        self.__serializer.serialize(self)

    def load(self, key):
        return self.__serializer.deserilize(key)

    @property
    def name(self):
        return self._name

    @property
    def members(self):
        return self._members

    @property
    def methods(self):
        return self._methods

    @property
    def parents(self):
        return self._base_classes