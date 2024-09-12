import time

from f import a, b, dx, efx, ex, f, fd, fdd, round_digits, x1
from gradient_descent import gradient_descent
from steepest_descent import steepest_descent


def main():
    t0 = time.time()
    for i in range(1000):
        steepest_descent(f, fd, a, b, ex, efx, x1, dx)
    t1 = time.time()
    total = t1 - t0
    print(total)


if __name__ == "__main__":
    main()
