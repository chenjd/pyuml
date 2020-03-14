from typed_ast import ast3


class ClassParser(ast3.NodeVisitor):
    """
    todo
    """
    # List to put the class data.
    puml_classes = list()

    def visit_Module(self, node):
        """
        :param node:
        :return:
        """
        for n in node.body:
            self.visit(n)

    def visit_ClassDef(self, node):
        """
        todo
        """
        print(node.name)

        class_dic = dict()
        class_dic['name'] = node.name
        class_dic['members'] = list()
        class_dic['methods'] = list()

        for child in node.body:
            if isinstance(child, ast3.FunctionDef):
                # private methods
                if child.name.startswith('__'):
                    class_dic['methods'].append('-' + child.name)
                else:
                    class_dic['methods'].append('+' + child.name)

                # constructor
                if child.name == '__init__':
                    for code in child.body:
                        if isinstance(code, ast3.Assign):
                            for target in code.targets:
                                if isinstance(target, ast3.Attribute):
                                    if isinstance(target.value, ast3.Name):
                                        if target.value.id == 'self':
                                            # private member
                                            if target.attr.startswith('__'):
                                                class_dic['members'].append('-' + target.attr)
                                            else:
                                                class_dic['members'].append('+' + target.attr)

        print(class_dic)

        ast3.NodeVisitor.generic_visit(self, node)

        return self.puml_classes

    def visit_FunctionDef(self, node):
        print(node.name)
        self.generic_visit(node)
