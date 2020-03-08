#!/usr/bin/env python
import os
import sys
import pydot
from pylint import run_pyreverse


class PyUML:
    def __init__(self):
        print('pyuml start')

    def run(self, args):
        run_pyreverse()
        self._render_with_pydot("classes.dot", "utf8")

    def _render_with_pydot(self, filename, encoding):
        graphs = pydot.graph_from_dot_file(filename, encoding=encoding)
        for g in graphs:
            path = os.path.abspath(os.getcwd()) + '/test.png'
            g.write_png(path)


def run_pyuml():
    """run pyuml"""
    PyUML().run(sys.argv[1:])


run_pyuml()
