from f import a, b, e, f, fd, fdd, round_digits

RATIO = (1 + 5**0.5) / 2


def newton_method(f, fd, fdd, a, b, e):
    x0 = (a + b) / 2
    xk = x0
    fdx = fd(xk)

    while abs(fdx) > e:
        xk = xk - fd(xk) / fdd(xk)
        fdx = fd(xk)

    return xk


def main():
    res = newton_method(f, fd, fdd, a, b, e)
    print(round(res, round_digits))


if __name__ == "__main__":
    main()
