from Lab02.f import a, b, e, f, fd, round_digits
from utils.log import clog

RATIO = (1 + 5**0.5) / 2
ROUND_TO = 2

def secant_method(f, fd, a, b, e):
    a = round(a, ROUND_TO)
    b = round(b, ROUND_TO)
    fda = fd(a)
    fdb = fd(b)
    xp = round(a - (fda / (fdb - fda)) * (b - a), ROUND_TO)
    fdxp = fd(xp)

    clog(f'a = {a}, b = {b}, fda = {fda}, fdb = {fdb}, xp = {xp}, fdxp = {fdxp}')

    while abs(fdxp) > e:
        if fdxp > 0:
            b = xp
            fdb = fdxp
        else:
            a = xp
            fda = fdxp
        xp = round(a - (fda / (fdb - fda)) * (b - a), ROUND_TO)
        fdxp = fd(xp)
        clog(f'a = {a}, b = {b}, fda = {fda}, fdb = {fdb}, xp = {xp}, fdxp = {fdxp}')
    
    fxp = f(xp)
    print(fxp)

    return fxp


def main():
    res = secant_method(f, fd, a, b, e)
    print(round(res, round_digits))


if __name__ == "__main__":
    main()
