#!/usr/bin/env python
# -*- coding: utf-8 -*-

from compiler.phases.code_generator import code_generator
from compiler.phases.tokenizer import tokenizer
from compiler.phases.transformer import transformer, visitor

from compiler.phases.parser import parser


def compiler(src_code):
    tokens = tokenizer(src_code)
    ast = parser(tokens)
    target_ast = transformer(ast, visitor)
    output = code_generator(target_ast)

    return output
