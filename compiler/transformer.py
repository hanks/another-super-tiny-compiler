#!/usr/bin/env python
# -*- coding: utf-8 -*-

from compiler.parser import Node
from compiler.utils import DotDict
from compiler.traverser import traverser


class TargetNode(object):
    Program = "Program"
    NumberLiteral = "NumberLiteral"
    StringLiteral = "StringLiteral"
    CallExpression = "CallExpression"
    Identifier = "Identifier"
    ExpressionStatement = "ExpressionStatement"

    def __init__(self, type, name=None, value=None, body=None, callee=None, arguments=None, expression=None):
        self.type = type
        self.name = name
        self.value = value
        self.body = body
        self.callee = callee
        self.arguments = arguments
        self.expression = expression

    def __str__(self):
        return """
type: {}
name: {}
value: {}
body: {}
callee: {}
arguments: {}
expression: {}
""".format(self.type, self.name, self.value, self.body, self.callee, self.arguments, self.expression)

    def __eq__(self, other):
        if type(other) is type(self):
            return self.__dict__ == other.__dict__

        return False

    def __ne__(self, other):
        if type(other) is type(self):
            return not self.__eq__(other)

        return True


def create_call_expression_target_node(node, parent):
    expression = TargetNode(
        TargetNode.CallExpression,
        callee=TargetNode(TargetNode.Identifier, name=node.name),
        arguments=[]
    )

    node._context = expression.arguments

    if parent.type != Node.CallExpression:
        expression = TargetNode(TargetNode.ExpressionStatement, expression=expression)

    return expression


visitor = {
    Node.NumberLiteral: DotDict({
        "enter": lambda node, parent: parent._context.append(TargetNode(TargetNode.NumberLiteral, value=node.value))
    }),
    Node.StringLiteral: DotDict({
        "enter": lambda node, parent: parent._context.append(TargetNode(TargetNode.StringLiteral, value=node.value))
    }),
    Node.CallExpression: DotDict({
        "enter": lambda node, parent: parent._context.append(
            create_call_expression_target_node(node, parent)
        )
    })
}


def transformer(ast, visitor):
    target_ast = TargetNode(TargetNode.Program, body=[])
    # _context is used to store new target nodes from the original one when traversing the original ast
    # and keep the same tree structure as original one
    ast._context = target_ast.body
    traverser(ast, visitor)

    return target_ast
