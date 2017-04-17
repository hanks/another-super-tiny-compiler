#!/usr/bin/env python
# -*- coding: utf-8 -*-


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
