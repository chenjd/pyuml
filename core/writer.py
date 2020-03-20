class DotWriter:
    """
    todo
    """

    def __init__(self):
        pass

    def write(self, classes):
        """
        todo
        """
        dot_string = "digraph \"class\" {\n"
        dot_string = self.write_node(dot_string, classes)
        dot_string = self.write_edge(dot_string, classes)
        dot_string += "}"
        print(dot_string)
        return dot_string

    def write_edge(self, dot_string, classes):
        """
        todo
        """
        for index in range(len(classes)):
            dot_string = self._write_relationship(dot_string, classes[index]["name"], classes[index]["base_classes"])
        return dot_string

    def write_node(self, dot_string, classes):
        """
        todo
        """
        for index in range(len(classes)):
            dot_string = self._write_class(dot_string, index, classes[index].name)
            dot_string = self._write_members(dot_string, classes[index].members)
            dot_string = self._write_methods(dot_string, classes[index].methods)
            dot_string += ",shape=\"record\"]"
            dot_string += ";\n"

        return dot_string

    def _write_class(self, dot_string, class_id, class_name):
        dot_string += "    \"{}\" [label=\"{{{}|".format(class_name, class_name)
        return dot_string

    def _write_members(self, dot_string, members):
        if len(members) == 0:
            return dot_string

        for member in members:
            dot_string += "{}\l".format(member)
        dot_string +="|"

        return dot_string

    def _write_methods(self, dot_string, methods):
        if len(methods) == 0:
            return dot_string

        for method in methods:
            dot_string += "{}\l".format(method)
        dot_string +="}\""

        return dot_string

    def _write_relationship(self, dot_string, class_name, relationship):
        if len(relationship) == 0:
            return dot_string
        for base in relationship:
            dot_string += "    \"{}\" -> \"{}\"[arrowhead = \"empty\", arrowtail = \"none\"]\n".format(class_name, base.id)


        return dot_string




