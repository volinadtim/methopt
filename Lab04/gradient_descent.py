import inspect
from utils.grad import grad, vector_abs
from utils.log import log


def gradient_descent(f, dfs, e, stepx):
    n = len(dfs)
    M = [0] * n
    gradf = grad(*dfs)
    print(*inspect.getsource(gradf))
    x = M
    while True:
        dx = gradf(*x)
        if vector_abs(*dx) <= e:
            return x
        x = [(x[i] - stepx * dx[i]) for i in range(n)]
