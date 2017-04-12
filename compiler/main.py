#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re


class Token(object):
    PAREN = "paren"
    NUMBER = "number"

    def __init__(self, type, value, params=None):
        self.type = type
        self.value = value
        self.params = params

    def __str__(self):
        return """
type: {}
value: {}
param: {}
""".format(self.type, self.value, self.params)

    def __eq__(self, other):
        if type(other) is type(self):
            return self.type == other.type and self.value == other.value and self.params == other.params

        return False

    def __ne__(self, other):
        if type(other) is type(self):
            return not self.__eq__(other)

        return True


class Pattern(object):
    WHITESPACE = r"\s"
    NUMBER = r"[0-9]"


def tokenizer(input):
    current = 0
    tokens = []

    while current < len(input):
        char = input[current]

        if char == "(":
            t = Token(Token.PAREN, "(")
            tokens.append(t)
            current += 1
            continue

        if char == ")":
            t = Token(Token.PAREN, ")")
            tokens.append(t)
            current += 1
            continue

        # ignore whitespace
        if re.match(Pattern.WHITESPACE, char):
            current += 1
            continue

        if re.match(Pattern.NUMBER, char):
            value = []
            while re.match(Pattern.NUMBER, char):
                value.append(char)
                current += 1
                char = input[current]

            t = Token(Token.NUMBER, "".join(value))
            tokens.append(t)
            continue

    return tokens
