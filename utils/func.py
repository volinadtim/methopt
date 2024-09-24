def invert(vars: list[float]):
    return [-i for i in vars]


def invert_func(func):
    return lambda *arg: -func(*arg)
