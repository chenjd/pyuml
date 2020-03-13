from ast import NodeVisitor, iter_fields, AST


class ClassParser(NodeVisitor):
    """
    todo
    """
    # List to put the class data.
    puml_classes = list()

    def visit_ClassDef(self, node):
        """
        todo
        """

        print(type(node).__name__)
        NodeVisitor.generic_visit(self, node)

        return self.puml_classes


class DotGenVisitor(NodeVisitor):
    """
    todo
    """

    @staticmethod
    def _qualified_name(obj):
        """
        """
        return "%s.%s" % (obj.__module__, obj.__name__)

    def label(self, node):
        """
        """
        pass
        # return r"%s\n%s" % (type(node).__name__, node.label())

    def generic_visit(self, node):

        # label this node
        out_string = 'n%s [label="%s"];\n' % (id(node), self.label(node))

        # edges to children
        for fieldname, fieldvalue in iter_fields(node):
            for index, child in self.enumerate_flatten(fieldvalue):
                if isinstance(child, AST):
                    suffix = "".join(["[%d]" % i for i in index])
                    out_string += 'n{} -> n{} [label="{}{}"];\n'.format(
                        id(node), id(child), fieldname, suffix)
                    out_string += self.visit(child)
        return out_string

    def enumerate_flatten(self, obj_or_list):
        if isinstance(obj_or_list, list):
            for n, gen in enumerate(map(self.enumerate_flatten, obj_or_list)):
                for k, elem in gen:
                    yield (n,) + k, elem
        else:
            yield (), obj_or_list
