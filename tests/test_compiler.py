#!/usr/bin/env python
# -*- coding: utf-8 -*-

from compiler.main import tokenizer, Token


def test_tokenizer():
    input = "(123 456)"
    result = tokenizer(input)

    token1 = Token(Token.PAREN, "(")
    token2 = Token(Token.NUMBER, "123")
    token3 = Token(Token.NUMBER, "456")
    token4 = Token(Token.PAREN, ")")
    expect = [token1, token2, token3, token4]

    assert expect == result
