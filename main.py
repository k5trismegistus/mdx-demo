import os
import sys
import glob

from lark import Lark
from lark.tree import Tree

from src import visitor

if __name__ == '__main__':

    rule = open('mdx/grammer.txt').read()
    parser = Lark(rule, start='component')


    components = dict()

    for component_file in glob.glob('./components/*.mdx'):
        filename = component_file.split('/')[-1]
        component_name = os.path.splitext(filename)[0]
        with open(component_file) as f:
            components[component_name] = parser.parse(f.read())

    root = components['Root']

    global_env = dict()

    _visitor = visitor.Visitor(components)
    result = _visitor.visit(root, global_env)

    print(result)
