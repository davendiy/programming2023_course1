#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 30.01.24
# Excusa. Quod scripsi, scripsi.

# by d.zashkonyi


from matrix import swap_rows_inplace, elem_transform, shape, copy_m, print_matrix


def gauss_elimination(matrix):

    n, m = shape(matrix)
    mul_coeff = 1

    for i in range(n):

        # find non-zero element below main diagonal
        for j in range(i, m):
            if matrix[j][i] != 0:
                mul_coeff *= swap_rows_inplace(matrix, i, j)
                break

        # perform elimination
        if matrix[i][i] != 0:
            for j in range(i+1, m):
                coeff = -matrix[j][i] / matrix[i][i]
                elem_transform(matrix, j, i, coeff)
    return mul_coeff


def rank(matrix):
    tmp = copy_m(matrix)
    gauss_elimination(tmp)

    res_rank = 0

    for row in matrix:
        if any(row):
            res_rank += 1
    return res_rank


def determinant(matrix):
    n, m = shape(matrix)
    if n != m:
        raise ValueError(f"Can't find determinant of non-square matrix: {(n, m)}")

    tmp = copy_m(matrix)
    res = gauss_elimination(tmp)
    for i in range(n):
        res *= matrix[i][i]
    return res


if __name__ == "__main__":
    test_matrix = [
        [1, 2, 3],
        [2, 2, 8],
        [3, 2, 2]
    ]

    gauss_elimination(test_matrix)
    print_matrix(test_matrix)
