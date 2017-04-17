#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

from compiler.exceptions import InvalidTokenTypeError
from compiler.models.token import Token


class Pattern(object):
    WHITESPACE = r"\s"
    NUMBER = r"[0-9]"
    DOUBLE_QUOTE = r"\""
    NAME = r"[A-Z]"

    # pre compile patterns for optimization
    whitespace = re.compile(WHITESPACE)
    number = re.compile(NUMBER)
    double_quote = re.compile(DOUBLE_QUOTE)
    # case-insensitive for name type
    name = re.compile(NAME, re.I)


def tokenizer(input):
    current = 0
    tokens = []
    length = len(input)

    while current < length:
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
        if Pattern.whitespace.match(char):
            current += 1
            continue

        if Pattern.number.match(char):
            value = []
            while Pattern.number.match(char):
                value.append(char)
                current += 1
                if current >= length:
                    break
                char = input[current]

            t = Token(Token.NUMBER, "".join(value))
            tokens.append(t)
            continue

        if Pattern.double_quote.match(char):
            value = []
            # skip start double quote
            current += 1
            char = input[current]

            while not Pattern.double_quote.match(char):
                value.append(char)
                current += 1
                if current >= length:
                    break
                char = input[current]

            # skip end double quote
            current += 1
            t = Token(Token.STRING, "".join(value))
            tokens.append(t)
            continue

        if Pattern.name.match(char):
            value = []
            while Pattern.name.match(char):
                value.append(char)
                current += 1
                if current >= length:
                    break
                char = input[current]

            t = Token(Token.NAME, "".join(value))
            tokens.append(t)
            continue

        raise InvalidTokenTypeError()

    return tokens
