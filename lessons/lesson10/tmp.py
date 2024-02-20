#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 03.12.23
# Excusa. Quod scripsi, scripsi.

# by d.zashkonyi


def res(pol):
    start = 0
    coef_array = {}
    for i in range(len(pol)):
        if pol[i] == 'x':
            coef = pol[start:i]
            coef = to_numb(coef)
            for x in range(i, len(pol)):
                if pol[x] == '^':
                    try:
                        if pol.get(x+1, '0') == '1' and pol.get(x+2, '0') == '0':
                            coef_array[10] = coef
                            break
                    except IndexError:
                            coef_array[int(pol[x + 1])] = coef
                            break
                    else:
                        coef_array[int(pol[x + 1])] = coef
                        break
            start = i + 1
    return coef_array


def to_numb(string):
    if '+' in string:
        plus = string.index('+')
        deg = string[plus + 1:]
    elif '-' in string:
        plus = string.index('-')
        deg = string[plus:]
    else:
        return string
    return deg


def norm(pol):
    new = ''
    if pol[-1] == 'x':
        new += pol + '^1'
    else:
        for x in range(len(pol)-1):
            if pol[x] == 'x' and (pol[x+1] == '+' or pol[x+1] == '-'):
                new += pol[:x+1] + '^1' + pol[x+1:]
                break
    if new == '':
        new = pol
    if new[-2] != '^' and new[-3] != '^':
        new += 'x^0'
    return new


def multiplication(pol1, pol2):
    new = [0] * 21
    for x in range(len(pol1)):
        for i in range(len(pol2)) :
            if new[x+i] == 0:
                new[x+i] = int(pol1[x]) * int(pol2[i])
            else:
                new[x+i] += int(pol1[x]) * int(pol2[i])
    return new


def change(pol):
    for x in range(len(pol)):
        if pol[x] == '':
            pol[x] = '1'
        elif pol[x] == '-':
            pol[x] = '-1'
    return pol


def answer(pol):
    new = '+'
    for x in range(len(pol)-1,-1,-1):
        if pol[x] != 0:
            new += str(pol[x]) + 'x^' + str(x) + '+'
    return new


polynomial1 = input()
polynomial2 = input()
if polynomial2 == '0'or polynomial1 == '0':
    print(0)
else:
    coef1 = change(res(norm(polynomial1)))
    coef2 = change(res(norm(polynomial2)))
    s = multiplication(coef1, coef2)
    res = answer(s).replace('x^0+','')
    res = res.replace('^1+', '+')
    res = res.replace('+-', '-')
    res = res.replace('+1x', 'x')
    res = res.replace('-1x', 'x')
    if res[0] == '+':
        res = res[1:]
    if res[-1] == '+':
        res = res[:-1]
    if res[0] == '1' and res[1] == 'x':
        res = res[1:]
    print(res)
