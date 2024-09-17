from constants import VERBOSE


def log(*arg):
    if VERBOSE:
        print(*arg)
