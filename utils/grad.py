from typing import Callable


def grad(*args: Callable[[list[float]], float]) -> Callable[[list[float]], list[float]]:
    dfs = args

    def grad_function(*args: list[float]) -> list[float]:
        vars = args
        vars_count = len(vars)
        assert vars_count == len(dfs)
        return [dfs[i](*vars) for i in range(vars_count)]

    return grad_function


def vector_abs(*args) -> float:
    vars = args
    return sum(i**2 for i in vars) ** 0.5


def normalize(vars) -> list[float]:
    abs = vector_abs(*vars)
    return [i / abs for i in vars]
