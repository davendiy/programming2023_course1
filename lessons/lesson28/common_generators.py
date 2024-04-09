
from typing import Iterable


def flatten(seq, ignore_types=(str, bytes)):
    if isinstance(seq, Iterable) and not isinstance(seq, ignore_types):
        for el in seq:
            yield from flatten(el)
    else:
        yield seq


def chain(*list_of_seq):
    for seq in list_of_seq:
        yield from seq


def own_zip(*list_of_seq):
    iters = [iter(seq) for seq in list_of_seq]
    while True:
        try:
            yield [next(seq) for seq in iters]
        except StopIteration:
            break


if __name__ == '__main__':
    test = [1, 2, [3, 4], [5, 6, 7], [8, [9, 10], [11], 'strsdkjfgh', {12, 13, 14}]]
    for el in flatten(test):
        print(el)

    for el in chain(range(1, 10), range(1, 100)):
        print(el)

    for x, y, z in own_zip(range(1, 10), range(-5, 5), range(10, 15)):
        print(x, y, z)
