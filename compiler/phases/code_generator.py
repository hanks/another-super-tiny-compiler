#!/usr/bin/env python
# -*- coding: utf-8 -*-

from compiler.exceptions import InvalidTargetNodeTypeError
from compiler.phases.transformer import TargetNode


def code_generator(node):
    if node.type == TargetNode.Program:
        return "\n".join(map(code_generator, node.body))
    elif node.type == TargetNode.ExpressionStatement:
        return code_generator(node.expression) + ";"
    elif node.type == TargetNode.CallExpression:
        return code_generator(node.callee) + "(" + ", ".join(map(code_generator, node.arguments)) + ")"
    elif node.type == TargetNode.Identifier:
        return node.name
    elif node.type == TargetNode.NumberLiteral:
        return node.value
    elif node.type == TargetNode.StringLiteral:
        return "\"" + node.value + "\""
    else:
        raise InvalidTargetNodeTypeError()
