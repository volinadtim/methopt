from Lab02.f import a, b, e, f, fd, fdd, round_digits
from utils.log import clog

RATIO = (1 + 5**0.5) / 2


def newton_method(f, fd, fdd, a, b, e):
    x0 = (a + b) / 2
    xk = x0
    fdx = fd(xk)
    i = 0
    clog(f'x{i} = {xk}, fdx = {fdx}, fdd(xk) = {fdd(xk)}')

    while abs(fdx) > e:
        i += 1
        xk = xk - fd(xk) / fdd(xk)
        fdx = fd(xk)
        clog(f'x{i} = {xk}, fdx = {fdx}, fdd(xk) = {fdd(xk)}')

    return xk


def main():
    res = newton_method(f, fd, fdd, a, b, e)
    print(round(res, round_digits))


if __name__ == "__main__":
    main()
