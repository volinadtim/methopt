from constants import VERBOSE


def clog(*arg, verbose=VERBOSE):
    if verbose:
        print(*arg)
