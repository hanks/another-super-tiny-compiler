#!/usr/bin/env python
# -*- coding: utf-8 -*-

from compiler.models.node import Node
from compiler.models.target_node import TargetNode
from compiler.phases.traverser import traverser
from compiler.utils.utils import DotDict


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
