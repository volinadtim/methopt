from f import a, b, e, f, round_digits

RATIO = (1 + 5**0.5) / 2


def golden_ratio_method(f, a, b, e):
    x1 = b - (b - a) / RATIO
    x2 = a + (b - a) / RATIO

    fx1 = f(x1)
    fx2 = f(x2)

    while x2 - x1 >= e:
        if fx1 < fx2:
            b = x2
            x1, x2 = b - (b - a) / RATIO, x1
            fx1, fx2 = f(x1), fx1
        else:
            a = x1
            x1, x2 = x2, a + (b - a) / RATIO
            fx1, fx2 = fx2, f(x2)

    return (x1 + x2) / 2


def main():
    res = golden_ratio_method(f, a, b, e)
    print(round(res, round_digits))


if __name__ == "__main__":
    main()
