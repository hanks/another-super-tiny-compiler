#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Node(object):
    NumberLiteral = "NumberLiteral"
    StringLiteral = "StringLiteral"
    CallExpression = "CallExpression"
    Program = "Program"

    def __init__(self, type, name=None, value=None, body=None, params=None):
        self.type = type
        self.name = name
        self.value = value
        self.body = body
        self.params = params

    def __str__(self):
        return """
type: {}
name: {}
value: {}
body: {}
params: {}
""".format(self.type, self.name, self.value, self.body, self.params)

    def __eq__(self, other):
        if type(other) is type(self):
            return self.__dict__ == other.__dict__

        return False

    def __ne__(self, other):
        if type(other) is type(self):
            return not self.__eq__(other)

        return True
