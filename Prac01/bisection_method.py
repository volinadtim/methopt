from f import a, b, e, f, round_digits


def _iterate_left(a, b, e):
    return (a + b - e) / 2


def _iterate_right(a, b, e):
    return (a + b + e) / 2


def bisection_method(f, a, b, e):
    x1 = a
    x2 = b

    while (b - a) > 2 * e:
        x1 = _iterate_left(a, b, e)
        x2 = _iterate_right(a, b, e)
        if f(x1) < f(x2):
            b = x2
        else:
            a = x1

    return (a + b) / 2


def main():
    res = bisection_method(f, a, b, e)
    print(round(res, round_digits))


if __name__ == "__main__":
    main()
