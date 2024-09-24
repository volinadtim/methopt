def sum_vector(vector1: list[float], vector2: list[float]) -> list[float]:
    n = len(vector1)
    assert n == len(vector2)
    return [vector1[i] + vector2[i] for i in range(n)]


def coef_multiply(a: float, vector: list[float]) -> list[float]:
    return [a * i for i in vector]


def scalar_multiply(vector1: list[float], vector2: list[float]) -> list[float]:
    n = len(vector1)
    assert n == len(vector2)
    return [vector1[i] * vector2[i] for i in range(n)]


def vector_abs(*args) -> float:
    vars = args
    return sum(i**2 for i in vars) ** 0.5


def normalize(vars) -> list[float]:
    abs = vector_abs(*vars)
    return [i / abs for i in vars]
