#!/usr/bin/env python
# -*- coding: utf-8 -*-


from compiler.models.token import Token
from compiler.models.node import Node
from compiler.exceptions import InvalidTokenTypeError


def walk(tokens, current):
    if current >= len(tokens):
        return None, current

    token = tokens[current]

    if token.type == Token.NUMBER:
        node = Node(Node.NumberLiteral, value=token.value)
        return node, current + 1

    if token.type == Token.STRING:
        node = Node(Node.StringLiteral, value=token.value)
        return node, current + 1

    if token.type == Token.PAREN and token.value == "(":
        # skip left paren
        current += 1
        token = tokens[current]

        node = Node(Node.CallExpression, name=token.value, params=[])

        # add params
        current += 1
        token = tokens[current]

        while (token.type != Token.PAREN) or (token.type == Token.PAREN and token.value != ")"):
            child_node, current = walk(tokens, current)
            if child_node is None:
                break
            node.params.append(child_node)
            token = tokens[current]

        return node, current + 1

    raise InvalidTokenTypeError()


def parser(tokens):
    ast = Node(type=Node.Program, body=[])

    current = 0

    while current < len(tokens):
        node, current = walk(tokens, current)
        ast.body.append(node)

    return ast
