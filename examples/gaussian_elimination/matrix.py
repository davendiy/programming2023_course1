#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 30.01.24
# Excusa. Quod scripsi, scripsi.

# by d.zashkonyi


def _is_matrix(matrix):
    if not isinstance(matrix, list):
        raise ValueError("matrix should be two-dimensional array")
    elif not isinstance(matrix[0], list):
        raise ValueError("matrix should be two-dimensional array")
    elif any(not isinstance(row, list) for row in matrix):
        raise ValueError("matrix should be two-dimensional array")
    elif any(len(row) != len(matrix[0]) for row in matrix):
        raise ValueError("matrix should be two-dimensional array with rows of same length")


def shape(matrix: list, safe=False):
    if not safe:
        _is_matrix(matrix)
    return len(matrix), len(matrix[0])


def copy_m(matrix, safe=False):
    if not safe:
        _is_matrix(matrix)

    n, m = shape(matrix, safe=True)

    return [
        [matrix[i][j] for j in range(m)]
        for i in range(n)
    ]


def swap_rows_inplace(matrix, i, j):

    _is_matrix(matrix)
    matrix[i], matrix[j] = matrix[j], matrix[i]
    return 1 if i == j else -1


def swap_columns_inplace(matrix, i, j):

    _is_matrix(matrix)
    for k in range(shape(matrix)[1]):
        matrix[k][i], matrix[k][j] = matrix[k][j], matrix[i]
    return 1 if i == j else -1


def swap_rows_copy(matrix, i, j):

    _is_matrix(matrix)
    res = copy_m(matrix)
    swap_rows_inplace(res, i, j)
    return res


def get_row(matrix, i):

    _is_matrix(matrix)
    return matrix[i]


def get_column(matrix, j):

    _is_matrix(matrix)
    n, m = shape(matrix)
    return [
        matrix[i][j] for i in range(n)
    ]


def scalar_product(vec1, vec2):

    return sum(x * y for x, y in zip(vec1, vec2))


def dot_product(matrix1, matrix2):

    _is_matrix(matrix1)
    _is_matrix(matrix2)
    n1, m1 = shape(matrix1)
    n2, m2 = shape(matrix2)

    if m1 != n2:
        raise ValueError(f"Can't multiply matrices of shapes {(n1, m1)} and {(n2, m2)}.")

    return [
        [
            scalar_product(get_row(matrix1, i), get_column(matrix2, j))
            for j in range(m2)
        ]
        for i in range(n1)
    ]


def mul_vec(vector, a):
    return [x * a for x in vector]


def sum_vec(vec1, vec2):
    return [x + y for x, y in zip(vec1, vec2)]


def elem_transform(matrix, i, j, a):
    """Perform elementary transformation on matrix _inplace_:

    matrix[i] = matrix[i] + matrix[j] * a
    """
    matrix[i] = sum_vec(
        matrix[i], mul_vec(matrix[j], a)
    )


def print_matrix(matrix):
    max_len = 0
    for row in matrix:
        for el in row:
            if (cur_len := len(f'{el:.2f}')) > max_len:
                max_len = cur_len

    for row in matrix:
        row = ' '.join([f'{el:.2f}'.rjust(max_len, ' ') for el in row])
        print(row)
