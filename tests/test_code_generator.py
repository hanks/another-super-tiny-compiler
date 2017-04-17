#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from compiler.transformer import TargetNode
from compiler.exceptions import InvalidTargetNodeTypeError
from compiler.code_generator import code_generator


def test_code_generator_exception():
    node = TargetNode("ad-hoc-type")
    with pytest.raises(InvalidTargetNodeTypeError):
        code_generator(node)


def test_code_generator_string():
    node = TargetNode(TargetNode.StringLiteral, value="abc")
    result = code_generator(node)
    expect = "\"abc\""
    assert expect == result


def test_code_generator_number():
    node = TargetNode(TargetNode.NumberLiteral, value="2")
    result = code_generator(node)
    expect = "2"
    assert expect == result


def test_code_generator_identifier():
    node = TargetNode(TargetNode.Identifier, name="add")
    result = code_generator(node)
    expect = "add"
    assert expect == result


def test_code_generator_call_expression():
    node = TargetNode(
        TargetNode.CallExpression,
        callee=TargetNode(TargetNode.Identifier, name="subtract"),
        arguments=[
            TargetNode(TargetNode.NumberLiteral, value="4"),
            TargetNode(TargetNode.NumberLiteral, value="2"),
        ]
    )
    result = code_generator(node)
    expect = "subtract(4, 2)"
    assert result == expect


def test_code_generator_expression_statement():
    node = TargetNode(
        TargetNode.ExpressionStatement,
        expression=TargetNode(
            TargetNode.CallExpression,
            callee=TargetNode(TargetNode.Identifier, name="add"),
            arguments=[
                TargetNode(TargetNode.NumberLiteral, value="2"),
                TargetNode(TargetNode.NumberLiteral, value="4"),
            ]
        )
    )
    result = code_generator(node)
    expect = "add(2, 4);"
    assert result == expect


def test_code_generator_program():
    node = TargetNode(TargetNode.Program, body=[
        TargetNode(
            TargetNode.ExpressionStatement,
            expression=TargetNode(
                TargetNode.CallExpression,
                callee=TargetNode(TargetNode.Identifier, name="add"),
                arguments=[
                    TargetNode(TargetNode.NumberLiteral, value="2"),
                    TargetNode(
                        TargetNode.CallExpression,
                        callee=TargetNode(TargetNode.Identifier, name="subtract"),
                        arguments=[
                            TargetNode(TargetNode.NumberLiteral, value="4"),
                            TargetNode(TargetNode.NumberLiteral, value="2"),
                        ]
                    )
                ]
            )
        ),
        TargetNode(
            TargetNode.ExpressionStatement,
            expression=TargetNode(
                TargetNode.CallExpression,
                callee=TargetNode(TargetNode.Identifier, name="add"),
                arguments=[
                    TargetNode(TargetNode.NumberLiteral, value="2"),
                    TargetNode(TargetNode.NumberLiteral, value="4"),
                ]
            )
        )
    ])
    result = code_generator(node)
    expect = "add(2, subtract(4, 2));\nadd(2, 4);"
    assert result == expect
