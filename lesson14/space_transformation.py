#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 30.11.23
# Excusa. Quod scripsi, scripsi.

# by d.zashkonyi

import gc
from math import ceil

from some_module import dot

gc.collect()


our_dot = dot
del dot

A = [
    [1, 1, 1, 1, 8],
    [1, 0, 1, 1, 8],
    [1, 1, 1, 3, 8],
    [1, 1, 1, 1, 1],
    [1, 1, 4, 1, 8],
]


B = [
    [-1, 1, 1, 1, 8],
    [0, 0, 1, 1, 8],
    [1, 1, 1, 3, 8],
    [0, 1, 2, 1, 1],
    [1, 1, 4, 9, 8],
]


dot(A, B)
