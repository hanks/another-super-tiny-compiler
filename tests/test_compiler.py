#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from compiler.main import tokenizer, Token
from compiler.exceptions import InvalidTokenTypeError


def test_tokenizer_paren():
    input = "()"
    result = tokenizer(input)

    token1 = Token(Token.PAREN, "(")
    token2 = Token(Token.PAREN, ")")
    expect = [token1, token2]

    assert result == expect


def test_tokenizer_number():
    input = "123"
    result = tokenizer(input)

    token1 = Token(Token.NUMBER, "123")
    expect = [token1]

    assert result == expect


def test_tokenizer_space():
    input = "  "
    result = tokenizer(input)

    expect = []

    assert result == expect


def test_tokenizer_string():
    input = "\"abc\""
    result = tokenizer(input)

    token1 = Token(Token.STRING, "abc")
    expect = [token1]

    assert expect == result


def test_tokenizer_name():
    input = "abcD"
    result = tokenizer(input)

    token1 = Token(Token.NAME, "abcD")
    expect = [token1]

    assert expect == result


def test_invalid_token_type_error():
    input = "----"

    with pytest.raises(InvalidTokenTypeError):
        tokenizer(input)
