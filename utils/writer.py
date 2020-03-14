def normalize_node_id(nid):
    """Returns a suitable DOT node id for `nid`."""
    return '"%s"' % nid


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

    def write_edge(self, name1, name2, **props):
        """emit an edge from <name1> to <name2>.
        edge properties: see http://www.graphviz.org/doc/info/attrs.html
        """
        attrs = ['%s="%s"' % (prop, value) for prop, value in props.items()]
        n_from, n_to = normalize_node_id(name1), normalize_node_id(name2)
        self.emit("%s -> %s [%s];" % (n_from, n_to, ", ".join(sorted(attrs))))

    def write_node(self, name, **props):
        """emit a node with given properties.
        node properties: see http://www.graphviz.org/doc/info/attrs.html
        """
        attrs = ['%s="%s"' % (prop, value) for prop, value in props.items()]
        self.emit("%s [%s];" % (normalize_node_id(name), ", ".join(sorted(attrs))))
