from Lab03.f import a, b, dx, efx, ex, f, fd, x1
from Lab03.square_interpolation import square_interpolation
from utils.speed_test import speed_test


def square_interpolation_speed_test():
    speed_test(lambda: square_interpolation(f, fd, a, b, ex, efx, x1, dx))


if __name__ == "__main__":
    square_interpolation_speed_test()
