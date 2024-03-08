#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 30.01.24
# Excusa. Quod scripsi, scripsi.

# by d.zashkonyi

from matrix import shape, copy_m, swap_rows_copy, swap_rows_inplace, elem_transform


def test_shape():
    test_matrix = [[1]]
    assert shape(test_matrix) == (1, 1)

    test_matrix = [
        [1, 2, 3],
        [2, 2, 8],
        [3, 2, 2]
    ]

    assert shape(test_matrix) == (3, 3)

    try:
        shape('sdfjhsd')
    except ValueError:
        assert True
    except Exception as e:
        print('test failed')
        raise e
