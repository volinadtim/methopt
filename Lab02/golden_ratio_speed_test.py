import time

from Lab02.f import a, b, e, f
from Lab02.golden_ratio_method import golden_ratio_method
from utils import speed_test


def main():
    speed_test(lambda: golden_ratio_method(f, a, b, e))


if __name__ == "__main__":
    main()
