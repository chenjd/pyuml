class DotWriter:
    """

    """

    def __init__(self, config):
        self.styles = [
            dict(arrowtail="none", arrowhead="open"),
            dict(arrowtail="none", arrowhead="empty"),
            dict(arrowtail="node", arrowhead="empty", style="dashed"),
            dict(
                fontcolor="green", arrowtail="none", arrowhead="diamond", style="solid"
            ),
        ]

    def set_printer(self, file_name, basename):
        """initialize DotWriter and add options for layout.
        """
        layout = dict(rankdir="BT")
        self.file_name = file_name

    def get_title(self, obj):
        """get project title"""
        return obj.title

    def get_values(self, obj):
        """get label and shape for classes.
        The label contains all attributes and methods
        """
        label = obj.title
        if obj.shape == "interface":
            label = "«interface»\\n%s" % label
        label = r"%s|%s\l|" % (label, r"\l".join(obj.attrs))
        for func in obj.methods:
            if func.args.args:
                args = [arg.name for arg in func.args.args if arg.name != "self"]
            else:
                args = []
            label = r"%s%s(%s)\l" % (label, func.name, ", ".join(args))
        label = "{%s}" % label
        return dict(label=label, shape="record")

    def close_graph(self):
        """print the dot graph into <file_name>"""
        self.printer.generate(self.file_name)