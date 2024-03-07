#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Модуль призначено для перевірки синтаксичної правильності виразу та присвоєння.

Вираз може мати вигляд:
>>> (abc + 123.5)*d2-3/(x+y)

Вираз може містити:
    - змінні - ідентифікатори
    - константи - дійсні або цілі числа без знаку
    - знаки операцій: +, -, *, /
    - дужки: (, )

Присвоєння - це рядок виду

<змінна> = <вираз>

наприклад
>>> x = a + b

Функція `check_expression_syntax` за заданим списком токенів
для виразу має повернути булівське значення та (можливо) помилку

Кожний токен - це кортеж: (<тип токену>, <значення токену>)
Перевірка робиться на допустимість сусідніх токенів,
правильний перший та останній токен, порожній вираз,
правильність розставлення дужок.

Функція `check_assignment_syntax` за заданим списком токенів
для присвоєння має повернути булівське значення та (можливо) помилку.
"""

from tokenizer import get_tokens, Token

# словник множин допустимих наступних токенів для заданого токена
VALID_PAIRS = {
    "variable": {"operation", "right_paren"},
    "constant": {"operation", "right_paren"},
    "operation": {"variable", "constant", "left_paren"},
    "equal": {"variable", "constant", "left_paren"},
    "left_paren": {"left_paren", "variable", "constant"},
    "right_paren": {"right_paren", "operation"},
    "other": set()
    }


# словник помилок
ERRORS = {
    "invalid_pair": "Недопустима пара токенів {}, {}",
    "incorrect_parens": "Неправильно розставлені дужки",
    "empty_expr": "Порожній вираз",
    "incorrect_assignment": "Неправильне присвоєння",
    "invalid_start": 'Недопустимий початок або кінець'
    }

# кортеж допустимих перших токенів
VALID_START = ('variable', 'constant', 'left_paren')

# кортеж допустимих останніх токенів
VALID_END = ('variable', 'constant', 'right_paren')


def check_assignment_syntax(tokens):
    """Функція перевіряє синтаксичну правильність присвоєння за списком токенів.

    Повертає True/False та рядок помилки.
    Якщо помилки немає, то повертає порожній рядок.
    Використовує функцію check_expression_syntax
    
    :param tokens: список токенів типу Token (див. tokenizer.py)
    :return: 
        success: булівське значення
        error: рядок помилки
    """
    pass


def check_expression_syntax(tokens):
    """Функція перевіряє синтаксичну правильність виразу за списком токенів.

    Повертає True/False та рядок помилки.
    Якщо помилки немає, то повертає порожній рядок
    
    :param tokens: список токенів типу Token (див. tokenizer.py)
    
    :return:
        success: булівське значення
        error: рядок помилки
    """
    pass 


def _check_parens(tokens):
    """Функція перевіряє чи правильно розставлені дужки у виразі.
    
    Повертає True/False.
    :param tokens: список токенів
    :return: success - булівське значення
    """
    pass 


def _check_pair(token, next_token):
    """Функція перевіряє чи правильна пара токенів.
    
    Повертає True/False.
    
    :param token: поточний токен
    :param next_token: наступний токен
    :return: success - булівське значення
    """
    pass 


def _check_start_end(tokens):
    """Функція перевіряє чи правильний токен стоїть на початку та кінці 
    заданого виразу.
    
    :param tokens: список токенів 
    :return: success -- True/False
    """
    pass 


if __name__ == "__main__":
    success1, error1 = check_expression_syntax(get_tokens("(((ab1_ - 345.56)(*/.2{_cde23"))
    success2, error2 = check_expression_syntax(get_tokens("(ab1_ - 345.56)*/.2_cde23"))
    success3, error3 = check_expression_syntax(get_tokens(" - 345.56*/.2_cde23"))
    success4, error4 = check_expression_syntax(get_tokens("2 - 345.56 *"))
    success5, error5 = check_expression_syntax(get_tokens("2 - .2"))
    success6, error6 = check_expression_syntax(get_tokens("   "))
    success7, error7 = check_expression_syntax(get_tokens("((abc -3 * b2) + d5 / 7)"))
    success8, error8 = check_assignment_syntax(get_tokens("x + y"))
    success9, error9 = check_assignment_syntax(get_tokens("x ="))
    success10, error10 = check_assignment_syntax(get_tokens("x = (a+b)"))
    success11, error11 = check_assignment_syntax(get_tokens("x = (a = b)"))
    success12, error12 = check_assignment_syntax(get_tokens("_sdf = ="))
    success13, error13 = check_expression_syntax(get_tokens("x = x"))
    
    assert not success1 and error1 == 'Неправильно розставлені дужки'
    assert not success2 and error2 == "Недопустима пара токенів Token(type='operation', value='*'), Token(type='operation', value='/')" 
    assert not success3 and not success4 
    assert not success5 and error5 == "Недопустима пара токенів Token(type='operation', value='-'), Token(type='other', value='.')" 
    assert not success6 and error6 == "Порожній вираз" 
    assert success7 and error7 == "" 
    assert not success8 and error8 == "Неправильне присвоєння" 
    assert not success9 and error9 == "Порожній вираз"
    assert success10 and error10 == ""
    assert not success11 and error11 == "Недопустима пара токенів Token(type='variable', value='a'), Token(type='equal', value='=')"
    assert not success12 and error12 == "Недопустимий початок або кінець"
    assert not success13 and error13 == "Недопустима пара токенів Token(type='variable', value='x'), Token(type='equal', value='=')"

    print("Success =", True)
