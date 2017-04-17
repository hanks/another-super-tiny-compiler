#!/usr/bin/env python
# -*- coding: utf-8 -*-

from compiler.main import compiler


def test_compiler():
    input = "(add 2 (subtract 4 2))"
    result = compiler(input)
    expect = "add(2, subtract(4, 2));"
    assert result == expect
