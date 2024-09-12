import math


def f(x1, x2, x3):
    return x1**2 + x2**2 + x3**2 - x1 * x2 + x1 - 2 * x3


def dfx1(x1, x2, x3):
    return 2 * x1 - x2 + 1


def dfx2(x1, x2, x3):
    return 2 * x2 - x1


def dfx3(x1, x2, x3):
    return 2 * x3 - 2


def fd(x):
    return (1 / math.cos(x)) ** 2 - 2 * math.cos(x)


def fdd(x):
    return 2 * ((math.tan(x) ** 2 + 1) * math.tan(x) + math.sin(x))


a = 0
b = math.pi / 4
e = 0.00001
ex = 0.03
efx = 0.0001
round_digits = 4
x1 = 1
dx = 0.01
