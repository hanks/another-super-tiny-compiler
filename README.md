[![Build Status](https://travis-ci.org/hanks/another-super-tiny-compiler.svg?branch=master)](https://travis-ci.org/hanks/another-super-tiny-compiler) [![Coverage Status](https://coveralls.io/repos/github/hanks/another-super-tiny-compiler/badge.svg)](https://coveralls.io/github/hanks/another-super-tiny-compiler)

# another-super-tiny-compiler

Python version of [the super tiny compiler](https://github.com/thejameskyle/the-super-tiny-compiler) project.

# Why

Just for study, and I am interested in compiler implementation, so I follow this tiny project to
study the basic ideas to implement a small compiler:)

# Implementation

In this project, the object is to transform `Lisp-style` code to `C-style` code. And there are four phases implemented:

* tokenizer, similar to `lexer` to generate token from source code
* parser, conduct tokens to AST(abstract syntax tree)
* transformer, change AST v1 to AST v2
* code generator, output target code from AST v2

# Demo

```
> compiler("(add 2 (subtract 4 2))")
add(2, subtract(4, 2));
```

# Licence

MIT Licence
