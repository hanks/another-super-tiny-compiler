#!/usr/bin/env python
# -*- coding: utf-8 -*-

from compiler.parser import Node
from compiler.exceptions import InvalidNodeTypeError


def traverse_node(node, parent, visitor):
    methods = visitor.get(node.type)

    if methods and hasattr(methods, "enter"):
        methods.enter(node, parent)

    if node.type == Node.Program:
        traverse_array(node.body, node, visitor)
    elif node.type == Node.CallExpression:
        traverse_array(node.params, node, visitor)
    elif node.type in (Node.NumberLiteral, Node.StringLiteral):
        pass
    else:
        raise InvalidNodeTypeError()

    if methods and hasattr(methods, "exit"):
        methods.exit(node, parent)


def traverse_array(arr, parent, visitor):
    for node in arr:
        traverse_node(node, parent, visitor)


def traverser(root, visitor):
    traverse_node(root, root, visitor)
