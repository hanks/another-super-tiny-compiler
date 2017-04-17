#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from compiler.models.token import Token

from compiler.exceptions import InvalidTokenTypeError
from compiler.phases.parser import Node, walk, parser


def test_node():
    node1 = Node(Node.NumberLiteral, value=5)
    node2 = Node(Node.NumberLiteral, value=5)

    assert node1 == node2

    node3 = Node(Node.NumberLiteral, value=6)
    assert node1 != node3

    node4 = Node(Node.StringLiteral, value="abc")
    assert node1 != node4


def test_walk_number():
    tokens = []
    tokens.append(Token(Token.NUMBER, value="2"))
    result = walk(tokens, 0)
    expect = (Node(Node.NumberLiteral, value="2"), 1)
    assert result == expect

    tokens = []
    tokens.append(Token(Token.NUMBER, value="2"))
    tokens.append(Token(Token.NUMBER, value="3"))
    result = walk(tokens, 0)
    expect = (Node(Node.NumberLiteral, value="2"), 1)
    assert result == expect
    result = walk(tokens, 1)
    expect = (Node(Node.NumberLiteral, value="3"), 2)
    assert result == expect


def test_walk_string():
    tokens = []
    tokens.append(Token(Token.STRING, value="abc"))
    result = walk(tokens, 0)
    expect = (Node(Node.StringLiteral, value="abc"), 1)
    assert result == expect

    tokens = []
    tokens.append(Token(Token.STRING, value="abc"))
    tokens.append(Token(Token.STRING, value="cdf"))
    result = walk(tokens, 0)
    expect = (Node(Node.StringLiteral, value="abc"), 1)
    assert result == expect
    result = walk(tokens, 1)
    expect = (Node(Node.StringLiteral, value="cdf"), 2)
    assert result == expect


def test_walk_paren():
    tokens = []
    tokens.append(Token(Token.PAREN, value="("))
    tokens.append(Token(Token.NAME, value="add"))
    tokens.append(Token(Token.NUMBER, value="2"))
    tokens.append(Token(Token.NUMBER, value="3"))
    tokens.append(Token(Token.PAREN, value=")"))

    result = walk(tokens, 0)
    expect = (Node(Node.CallExpression, name="add", params=[
        Node(Node.NumberLiteral, value="2"),
        Node(Node.NumberLiteral, value="3"),
    ]), 5)
    assert expect == result


def test_walk_empty():
    tokens = []
    current = 0
    result = walk(tokens, current)
    expect = (None, 0)
    assert result == expect


def test_walk_exception():
    with pytest.raises(InvalidTokenTypeError):
        tokens = [Token("ad-hoc-type", value="hello")]
        current = 0
        walk(tokens, current)


def test_parser():
    # (add 2 (subtract 4 2 ))
    tokens = []
    tokens.append(Token(Token.PAREN, value="("))
    tokens.append(Token(Token.NAME, value="add"))
    tokens.append(Token(Token.NUMBER, value="2"))
    tokens.append(Token(Token.PAREN, value="("))
    tokens.append(Token(Token.NAME, value="subtract"))
    tokens.append(Token(Token.NUMBER, value="4"))
    tokens.append(Token(Token.NUMBER, value="2"))
    tokens.append(Token(Token.PAREN, value=")"))
    tokens.append(Token(Token.PAREN, value=")"))

    result = parser(tokens)
    expect = Node(Node.Program, body=[
        Node(Node.CallExpression, name="add", params=[
            Node(Node.NumberLiteral, value="2"),
            Node(Node.CallExpression, name="subtract", params=[
                Node(Node.NumberLiteral, value="4"),
                Node(Node.NumberLiteral, value="2")
            ])
        ])
    ])
    assert result == expect
