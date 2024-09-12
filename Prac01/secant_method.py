from f import a, b, e, f, fd, round_digits

RATIO = (1 + 5**0.5) / 2


def secant_method(f, fd, a, b, e):
    fda = fd(a)
    fdb = fd(b)
    xp = a - (fda / (fdb - fda)) * (b - a)
    fdxp = fd(xp)

    while abs(fdxp) > e:
        if fdxp > 0:
            b = xp
            fdb = fdxp
        else:
            a = xp
            fda = fdxp
        xp = a - (fda / (fdb - fda)) * (b - a)
        fdxp = fd(xp)

    return xp


def main():
    res = secant_method(f, fd, a, b, e)
    print(round(res, round_digits))


if __name__ == "__main__":
    main()
