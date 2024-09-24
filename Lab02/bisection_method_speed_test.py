import time

from Lab02.f import a, b, e, f
from Lab02.bisection_method import bisection_method


def main():
    t0 = time.time()
    for i in range(1000):
        bisection_method(f, a, b, e)
    t1 = time.time()
    total = t1 - t0
    print(total)


if __name__ == "__main__":
    main()
