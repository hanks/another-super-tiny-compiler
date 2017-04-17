#!/usr/bin/env python
# -*- coding: utf-8 -*-

from compiler.phases.transformer import transformer, visitor
from compiler.models.target_node import TargetNode
from compiler.phases.parser import Node


def test_transformer():
    ast = Node(Node.Program, body=[
        Node(Node.CallExpression, name="add", params=[
            Node(Node.NumberLiteral, value="2"),
            Node(Node.CallExpression, name="subtract", params=[
                Node(Node.NumberLiteral, value="4"),
                Node(Node.NumberLiteral, value="2")
            ])
        ])
    ])

    result = transformer(ast, visitor)

    expect = TargetNode(TargetNode.Program, body=[
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
        )
    ])

    assert result == expect
