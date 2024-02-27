#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Модуль призначено для перевірки роботи модулів
- tokenizer
- syntax_analyzer
- storage

та обчислення значення простого виразу (сума доданків)
"""

from tokenizer import get_tokens
from syntax_analyzer import check_expression_syntax
import storage


def fill_storage(tokens):
    for tok in tokens:
        if tok.type == "variable":
            storage.add(tok.value)


def compute_sum(tokens):
    s = 0
    for tok in tokens:
        if tok.type == "constant":
            value = float(tok.value)
            s += value
        elif tok.type == "variable":
            value = storage.get(tok.value)
            s += value
    return s


expression = "5 + a + 3"
tokens = get_tokens(expression)

success, error = check_expression_syntax(tokens)

if success:
    fill_storage(tokens)
    storage.set("a", 2)
    s = compute_sum(tokens)
    success = s == 10

print("Success =", success)
