from typing import Callable


def grad(*args: Callable[[list[float]], float]) -> Callable[[list[float]], list[float]]:
    dfs = args

    def grad_function(*args: list[float]) -> list[float]:
        vars = args
        vars_count = len(vars)
        assert vars_count == len(dfs)
        return [dfs[i](*vars) for i in range(vars_count)]

    return grad_function
