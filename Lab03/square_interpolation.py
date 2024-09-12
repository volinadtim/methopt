import numpy as np


def square_interpolation(f, fd, a, b, ex, efx, x1, dx):
    x2 = x1 + dx
    fx1 = f(x1)
    fx2 = f(x2)
    if fx1 > fx2:
        x3 = x1 + 2 * dx
    else:
        x3 = x1 - dx
    fx3 = f(x3)

    while True:
        min_index = np.argmin([fx1, fx2, fx3])
        fxmin = [fx1, fx2, fx3][min_index]
        xmin = [x1, x2, x3][min_index]
        px = (
            (1 / 2)
            * ((x2**2 - x3**2) * fx1 + (x3**2 - x1**2) * fx2 + (x1**2 - x2**2) * fx3)
            / ((x2 - x3) * fx1 + (x3 - x1) * fx2 + (x1 - x2) * fx3)
        )
        fpx = f(px)

        if (abs((fxmin - fpx) / fpx) < efx) and (abs((xmin - px) / px) < ex):
            return px
        elif x1 <= px <= x3:
            dots = np.array([(x1, fx1), (x2, fx2), (x3, fx3), (px, fpx)])
            sorted_indices = np.argsort(dots[:, 0])
            dots = dots[sorted_indices]
            min_index = np.argmin(dots[:, 1])
            assert min_index == 1 or min_index == 2

            x1, fx1 = dots[min_index - 1]
            x2, fx2 = dots[min_index]
            x3, fx3 = dots[min_index + 1]
        else:
            x1 = px
            return square_interpolation(f, fd, a, b, ex, efx, x1, dx)
