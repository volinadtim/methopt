from Lab02.f import a, b, e, f, round_digits
from utils.log import clog
import math

ROUND_TO = 20000

def _iterate_left(a, b, e):
    return round((a + b - e) / 2, ROUND_TO)


def _iterate_right(a, b, e):
    return round((a + b + e) / 2, ROUND_TO)


def bisection_method(f, a, b, e, verbose=None):
    
    while (b - a) > 2 * e:
        clog(f'(b - a) = {round(b - a, ROUND_TO)}', verbose=verbose)
        clog(f'a = {a}, b = {b}', verbose=verbose)
        x1 = _iterate_left(a, b, e)
        x2 = _iterate_right(a, b, e)
        y1 = round(f(x1), ROUND_TO)
        y2 = round(f(x2), ROUND_TO)
        clog(f'x1 = {x1}, x2 = {x2}', verbose=verbose)
        clog(f'y1 = {y1}, y2 = {y2}', verbose=verbose)
        if y1 > y2:
            clog('y1 > y2', verbose=verbose)
            a = x1
        else:
            clog('y1 <= y2', verbose=verbose)
            b = x2
        clog('\n===\n', verbose=verbose)

    xm = (a + b) / 2
    ym = f(xm)

    clog(xm, ym, verbose=verbose)

    return xm


def main():
    res = bisection_method(f, a, b, e)
    print(round(res, round_digits))


if __name__ == "__main__":
    main()
