from Lab02.f import a, b, e, f, round_digits
from utils.line_dots import draw_dots
from utils.log import clog

RATIO = (1 + 5**0.5) / 2

ROUND_TO = 200


def golden_ratio_method(f, a, b, e):
    A = a
    B = b
    x1 = round(b - (b - a) / RATIO, ROUND_TO)
    x2 = round(a + (b - a) / RATIO, ROUND_TO)

    clog(f'x1 = {x1}, x2 = {x2}')

    fx1 = f(x1)
    fx2 = f(x2)

    clog(f'fx1 = {fx1}, fx2 = {fx2}')

    coords = [x1, x2]

    while b - a > e * 2:
        clog(f'b - a = {b - a}')
        if fx1 < fx2:
            print('y1 < y2')
            b = x2
            x1, x2 = round(b - (b - a) / RATIO, ROUND_TO), x1
            fx1, fx2 = f(x1), fx1
            coords.append(x1)
            clog(f'a = {a}, b = {b}, x1 = {x1}, x2 = {x2}, fx1 = {fx1}, fx2 = {fx2}')
        else:
            print('y1 >= y2')
            a = x1
            x1, x2 = x2, round(a + (b - a) / RATIO, ROUND_TO)
            fx1, fx2 = fx2, f(x2)
            coords.append(x2)
            clog(f'a = {a}, b = {b}, x1 = {x1}, x2 = {x2}, fx1 = {fx1}, fx2 = {fx2}')
        clog('\n===\n')

    clog(f'b - a = {b - a}')

    print((b + a) / 2)
    print(f((b + a) / 2))

    draw_dots(A, B, coords)

    return (b + a) / 2


def main():
    res = golden_ratio_method(f, a, b, e)
    print(round(res, round_digits))


if __name__ == "__main__":
    main()
