#!/usr/bin/env python
# -*- coding: utf-8 -*-

from compiler.tokenizer import tokenizer
from compiler.parser import parser
from compiler.transformer import transformer, visitor
from compiler.code_generator import code_generator


def compiler(src_code):
    tokens = tokenizer(src_code)
    ast = parser(tokens)
    target_ast = transformer(ast, visitor)
    output = code_generator(target_ast)

    return output
