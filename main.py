#!/usr/bin/env python
import sys
import pydot
from pylint import run_pyreverse
from graphviz import Source


class PyUML:
    def __init__(self):
        print('pyuml start')

    def run(self, args):
        run_pyreverse()
        # subprocess.run("pyreverse -AS -o png " + filePath + " -p " + fileName, shell=True,
        #                   cwd="path/to/output/directory")

        self._render_with_graphviz("classes.dot")

    def _render_with_graphviz(self, filename):
        src = Source('');
        src = src.from_file(filename)
        src.render(format='png', filename= "test6")


def run_pyuml():
    """run pyuml"""
    PyUML().run(sys.argv[1:])


run_pyuml()
