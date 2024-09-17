import numpy as np
from utils.log import log

iteration = 0


def square_interpolation(f, fd, a, b, ex, efx, x1, dx):
    global iteration
    x2 = x1 + dx
    fx1 = f(x1)
    fx2 = f(x2)
    if fx1 > fx2:
        x3 = x1 + 2 * dx
    else:
        x3 = x1 - dx
    fx3 = f(x3)

    while True:
        iteration += 1
        log(f"\nIteration {iteration}")
        log(f"x1 = {x1}, x2 = {x2}, x3 = {x3}")
        log(f"fx1 = {fx1}, fx2 = {fx2}, fx3 = {fx3}")

        min_index = np.argmin([fx1, fx2, fx3])
        fxmin = [fx1, fx2, fx3][min_index]
        xmin = [x1, x2, x3][min_index]
        px = (
            (1 / 2)
            * ((x2**2 - x3**2) * fx1 + (x3**2 - x1**2) * fx2 + (x1**2 - x2**2) * fx3)
            / ((x2 - x3) * fx1 + (x3 - x1) * fx2 + (x1 - x2) * fx3)
        )
        fpx = f(px)

        log(f"min_index = {min_index}")
        log(f"fxmin = {fxmin}, xmin = {xmin}")
        log(f"fpx = {fpx}, px = {px}")

        func_d = abs((fxmin - fpx) / fpx)
        x_d = abs((xmin - px) / px)

        log(f"func_d = {func_d}, efx = {efx}, ok = {func_d < efx}")
        log(f"x_d = {x_d}, ex = {ex}, ok = {x_d < ex}")

        if (func_d < efx) and (x_d < ex):
            return px
        elif x1 <= px <= x3:
            log(f"{x1} <= {px} <= {x3}")
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
