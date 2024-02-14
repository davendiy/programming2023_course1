#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 30.11.23
# Excusa. Quod scripsi, scripsi.

# by d.zashkonyi


def scalar_product(x, y):
    return sum(_x * _y for _x, _y in zip(x, y))


def dot(A, B):

    n1, m1 = len(A), len(A[0])
    n2, m2 = len(B), len(B[0])

    assert m1 == n2, f"Can't multiply matrices of shapes {n1, m1} and {n2, m2} "

    res = [[0 for _ in range(m2)] for _ in range(n1)]
    for i in range(n1):
        for j in range(m2):
            res[i][j] = scalar_product(A[i], [B[k][j] for k in range(m1)])

    return res


if __name__ == '__main__':

    print("===================================================")

    x1 = [
        [1, 2, 3],
        [2, 2, 8],
        [0, 1, 0]
    ]

    x2 = [
        [3, 2, 2],
        [1, 4, 8],
        [8, 2, 8]
    ]

    print(dot(x1, x2))

    print('=================================================')
