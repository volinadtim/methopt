from f import a, b, e, f, round_digits

Fs = {}


def F(n):
    if n in Fs:
        return Fs[n]
    res = round((1 / 5**0.5) * (((1 + 5**0.5) / 2) ** n - ((1 - 5**0.5) / 2) ** n))
    Fs[n] = res
    return res


def _iterate_left(a, b, n, k=1):
    return a + (F(n - 1 - k) / F(n + 1 - k)) * (b - a)


def _iterate_right(a, b, n, k=1):
    return a + (F(n - k) / F(n + 1 - k)) * (b - a)


def _hit_required_e(a, b, e) -> int:
    n = 1
    while (b - a) / F(n) > e:
        n += 1
    return n


def fibonacci_minimization(f, a, b, e):
    n = _hit_required_e(a, b, e)
    x1 = _iterate_left(a, b, n)
    x2 = _iterate_right(a, b, n)

    k = 2
    while k <= n - 2:
        if f(x1) < f(x2):
            b = x2
            x1, x2 = _iterate_left(a, b, n, k), x1
        else:
            a = x1
            x1, x2 = x2, _iterate_right(a, b, n, k)
        k += 1

    return (x1 + x2) / 2


def main():
    res = fibonacci_minimization(f, a, b, e)
    print(round(res, round_digits))


if __name__ == "__main__":
    main()
