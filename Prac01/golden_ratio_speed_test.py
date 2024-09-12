import time

from f import a, b, e, f
from golden_ratio_method import golden_ratio_method
from utils import speed_test


def main():
    speed_test(lambda: golden_ratio_method(f, a, b, e))


if __name__ == "__main__":
    main()
