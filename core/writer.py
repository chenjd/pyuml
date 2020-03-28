from core.parser import ClassRecorder


class DotWriter:
    """
    todo
    """

    def __init__(self):
        pass

    def write(self, classes):
        """ (list of ClassRecorder) -> str
        Return dot node and relationship string from list of ClassRecorder

        """
        assert isinstance(classes, list)
        dot_string = "digraph \"class\" {\n"
        dot_string = self.write_node(dot_string, classes)
        dot_string = self.write_edge(dot_string, classes)
        dot_string += "}"
        print(dot_string)
        return dot_string

    def write_edge(self, dot_string, classes):
        """ (str, list of ClassRecorder) -> str
        Return dot node relation string from list of ClassRecorder

        >>> writer = DotWriter()
        >>> writer.write_edge('dot_string', 1)
        Traceback (most recent call last):
        AssertionError
        >>> int_list = (1,2)
        >>> writer.write_edge('dot_string', int_list)
        Traceback (most recent call last):
        AssertionError
        >>> class_recorder_list = list((ClassRecorder('test1', list()), ClassRecorder('test2', list())))
        >>> writer.write_edge(1, class_recorder_list)
        Traceback (most recent call last):
        AssertionError
        >>> writer.write_edge('dot_string', class_recorder_list)
        'dot_string'
        """
        assert isinstance(classes, list) and isinstance(dot_string, str)
        for cls in classes:
            assert isinstance(cls, ClassRecorder)
            dot_string = self._write_relationship(dot_string, cls.name, cls.parents)
        return dot_string

    def write_node(self, dot_string, classes):
        """ (str, list of ClassRecorder) -> str
        Return dot node string from list of ClassRecorder.

        >>> writer = DotWriter()
        >>> writer.write_node('dot_string', 1)
        Traceback (most recent call last):
        AssertionError
        >>> int_list = (1,2)
        >>> writer.write_node('dot_string', int_list)
        Traceback (most recent call last):
        AssertionError
        >>> class_recorder_list = list((ClassRecorder('test1', list()), ClassRecorder('test2', list())))
        >>> writer.write_node(1, class_recorder_list)
        Traceback (most recent call last):
        AssertionError
        >>> writer.write_node('', class_recorder_list)
        '    "test1" [label="{test1}",shape="record"];\\n    "test2" [label="{test2}",shape="record"];\\n'
        """
        assert isinstance(classes, list) and isinstance(dot_string, str)
        for cls in classes:
            assert isinstance(cls, ClassRecorder)
            dot_string = self._write_class(dot_string, cls.name)
            dot_string = self._write_members(dot_string, cls.members)
            dot_string = self._write_methods(dot_string, cls.methods)
            dot_string += ",shape=\"record\"]"
            dot_string += ";\n"

        return dot_string

    def _write_class(self, dot_string, class_name):
        """
        >>> writer = DotWriter()
        >>> dot_string =''
        >>> writer._write_class(dot_string, 1)
        Traceback (most recent call last):
        AssertionError
        """
        assert isinstance(class_name, str)
        dot_string += "    \"{}\" [label=\"{{{}".format(class_name, class_name)
        return dot_string

    def _write_members(self, dot_string, members):
        """
        todo
        """
        assert isinstance(members, list)

        if len(members) == 0:
            return dot_string

        dot_string += "|"
        for member in members:
            dot_string += "{}\l".format(member)

        return dot_string

    def _write_methods(self, dot_string, methods):
        """
        todo
        """
        assert isinstance(methods, list)
        if len(methods) == 0:
            dot_string += "}\""
            return dot_string

        dot_string += "|"
        for method in methods:
            dot_string += "{}\l".format(method)
        dot_string += "}\""

        return dot_string

    def _write_relationship(self, dot_string, class_name, relationship):
        """
        todo
        """
        assert isinstance(relationship, list)
        if len(relationship) == 0:
            return dot_string
        for base in relationship:
            dot_string += "    \"{}\" -> \"{}\"[arrowhead = \"empty\", arrowtail = \"none\"]\n".format(class_name,
                                                                                                       base.id)

        return dot_string
