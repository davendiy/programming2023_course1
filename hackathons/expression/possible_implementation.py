#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 24.11.23
# Excusa. Quod scripsi, scripsi.

# by d.zashkonyi


def is_integer(expression: str):
    if not expression:
        return False
    elif expression.isdigit():
        return True
    elif expression[0] in ['-', '+'] and expression[1:].isdigit():
        return True
    else:
        return False


def is_float(expression: str):

    if is_integer(expression):
        return True
    elif expression.count('.') == 1  \
        and is_integer(expression.replace('.', '')):
        return True
    else:
        return False


def is_operator(expression: str):
    return len(expression) == 1 and expression in '+-*/'


def get_integer_v1(expression: str):
    if not expression or not is_integer(expression[0]):
        return '', expression

    i = 0
    while i + 1 <= len(expression) and is_integer(expression[:i+1]):
        i += 1

    return expression[:i], expression[i:]


def get_prefix(expression: str, filter_func: callable, min_len=1):
    if not expression or not filter_func(expression[:min_len]):
        return '', expression

    i = min_len - 1
    while i+1 <= len(expression) and filter_func(expression[:i+1]):
        i += 1
    if i == 0: i += 1
    return expression[:i], expression[i:]


def get_integer(expression: str):
    return get_prefix(expression, is_integer)


def get_float(expression: str):
    return get_prefix(expression, is_float, min_len=2)


def get_operator(expression: str):
    return get_prefix(expression, is_operator)


def get_par(expression: str):
    if expression and expression[0] in '()':
        return expression[0], expression[1:]
    else:
        return '', expression


def tokenize_v1(expression: str):
    res = []
    expression = expression.replace(' ', '')
    while expression:
        for func in [get_par, get_operator, get_float, get_integer]:
            match, expression = func(expression)
            if match:
                break
        else:
            raise ValueError(f'Bad expression: {expression}')
        res.append(match)
    return res


def tokenize(expression: str):
    expression = expression.replace(' ', '')
    while expression:
        for func in [get_par, get_operator, get_float, get_integer]:
            match, expression = func(expression)
            if match:
                break
        else:
            raise ValueError(f"Bad expression: {expression}")

        yield match


def check_parentheses(tokens: list):
    balance = 0

    for token in tokens:
        if token == '(':
            balance += 1
        elif token == ')':
            balance -= 1

        if balance < 0:
            break

    return not balance


def get_sub_expression(tokens: list):

    if not check_parentheses(tokens) or tokens[0] != '(':
        return []

    res = []
    balance = 1
    for token in tokens[1:]:
        if token == '(':
            balance += 1
        elif token == ')':
            balance -= 1

        if balance == 0:
            break
        res.append(token)

    return res


tokens = list(tokenize('(123+324*(234-23)+234.2342) - (.324 + 2)'))

print(get_sub_expression(tokens))
