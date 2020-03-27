from typed_ast import ast3
from typed_ast.ast3 import ClassDef, Module, FunctionDef


class ClassRecorder:
    """
    record the class data
    """
    def __init__(self, name, parents):  # type: String
        self._name = name
        self._members = list()
        self._methods = list()
        self._base_classes = parents

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def members(self):
        return self._members

    @members.setter
    def members(self, members):
        self._members = members

    @property
    def methods(self):
        return self._methods

    @methods.setter
    def methods(self, methods):
        self._methods = methods

    @property
    def parents(self):
        return self._base_classes

    @parents.setter
    def parents(self, parents):
        self._base_classes = parents


class ClassParser(ast3.NodeVisitor):
    """
    Parese the source code
    """

    def __init__(self):
        super().__init__()
        self.classes_list = list()

    def visit_Module(self, node):
        """
        :param node:
        :return:
        """
        assert isinstance(node, Module)
        for n in node.body:
            self.visit(n)

    def visit_ClassDef(self, node):
        """
        todo
        """
        assert isinstance(node, ClassDef)

        class_recorder = ClassRecorder(node.name, node.bases)

        for child in node.body:
            if isinstance(child, ast3.FunctionDef):
                # private methods
                type_comment = ""
                if child.type_comment is not None:
                    type_comment = " : " + child.type_comment
                if child.name.startswith('__'):
                    class_recorder.methods.append('-' + child.name + type_comment)
                else:
                    class_recorder.methods.append('+' + child.name + type_comment)

                # constructor
                if child.name == '__init__':
                    for code in child.body:
                        if isinstance(code, ast3.Assign):
                            # add type comment
                            type_comment = ""
                            if code.type_comment is not None:
                                type_comment = " : " + code.type_comment
                            for target in code.targets:
                                if isinstance(target, ast3.Attribute):
                                    if isinstance(target.value, ast3.Name):
                                        if target.value.id == 'self':
                                            # private member
                                            if target.attr.startswith('__'):
                                                class_recorder.members.append('-' + target.attr + type_comment)
                                            else:
                                                class_recorder.members.append('+' + target.attr + type_comment)

        assert isinstance(class_recorder, ClassRecorder)
        self.classes_list.append(class_recorder)
        ast3.NodeVisitor.generic_visit(self, node)

    def visit_FunctionDef(self, node):
        assert isinstance(node, FunctionDef)
        self.generic_visit(node)
