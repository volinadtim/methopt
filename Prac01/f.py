import math


def f(x):
    return math.tan(x) - 2 * math.sin(x)


def fd(x):
    return (1 / math.cos(x)) ** 2 - 2 * math.cos(x)


def fdd(x):
    return 2 * ((math.tan(x) ** 2 + 1) * math.tan(x) + math.sin(x))


a = 0
b = math.pi / 4
e = 0.03 / 100
round_digits = 2
