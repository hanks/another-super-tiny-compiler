#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Token(object):
    PAREN = "paren"
    NUMBER = "number"
    STRING = "string"
    NAME = "name"

    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return """
type: {}
value: {}
""".format(self.type, self.value)

    def __eq__(self, other):
        if type(other) is type(self):
            return self.type == other.type and self.value == other.value

        return False

    def __ne__(self, other):
        if type(other) is type(self):
            return not self.__eq__(other)

        return True
