import math
import random

EPS = 1e-9
MAX_ITERATIONS = 10_000_000

INF = 1e8


def linear(start=0.1, step=1e-4):
    delta = start
    for _ in range(MAX_ITERATIONS):
        if delta == 0:
            break
        yield delta
        delta -= step


def geometric(start=1, degree=2):
    delta = start
    for _ in range(MAX_ITERATIONS):
        yield delta
        delta /= degree


def harmonic():
    for n in range(1, MAX_ITERATIONS):
        yield 1 / n


def alternating_harmonic():
    mul = 1
    for n in range(1, MAX_ITERATIONS):
        yield mul / n
        mul = -mul


def random_harmonic():
    for n in range(1, MAX_ITERATIONS):
        delta = 1 / n
        rand = random.random()   # in [0, 1]
        yield (rand * 2 * delta) - delta


algos = {
    'linear': linear,
    'geometric': geometric,
    'harmonic': harmonic,
    'alt_harmonic': alternating_harmonic,
    'rand_harmonic': random_harmonic,
}


def limit(x0, function, algorithm='', eps=EPS, **kwargs):
    algo_gen = algos[algorithm]
    prev = None
    for delta in algo_gen(**kwargs):
        cur = function(x0 + delta)
        if prev is None:
            prev = cur
            continue

        # границя за властивістю фундаментальної послідовності
        if abs(cur - prev) < eps:
            break

        if cur > INF:
            return float('inf')
        elif cur < -INF:
            return float('-inf')

        prev = cur
    else:
        return None

    return cur


def derivative_v2(x0, function, algorithm='', eps=EPS, **kwargs):

    f0 = limit(x0, function, eps=eps, algorithm=algorithm)
    if f0 == float('inf'):
        return None

    def target(x):
        return (function(x) - f0) / (x - x0)

    return limit(x0, target, algorithm, eps, **kwargs)


def derivative(x0, function, algorithm='', eps=EPS, **kwargs):
    prev = function(x0)    # fixme: change
    algo_gen = algos[algorithm]
    for delta in algo_gen(**kwargs):
        cur = function(x0 + delta) - function(x0)
        cur = cur / delta

        if abs(cur - prev) < eps:
             break
        prev = cur
    else:
        return None
    return cur


def approx_derivative(x0, function, eps=EPS):
    # симетрична форма
    return (function(x0 + eps) - function(x0 - eps)) / (2 * eps)


x0 = 0
print(math.cos(x0))
print(derivative(x0, math.sin, algorithm='harmonic'))
print(derivative_v2(x0, math.sin, algorithm='harmonic'))


def f(x):
    return 1 / x

print(limit(0, f, algorithm='rand_harmonic'))
print(derivative_v2(0, f, algorithm='rand_harmonic'))
print(derivative(x0, math.sin, algorithm='rand_harmonic'))
print(approx_derivative(x0, math.sin))
print(approx_derivative(0, f))
