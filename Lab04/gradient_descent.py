import inspect
from utils.grad import grad
from utils.vector import vector_abs
from utils.log import clog


def gradient_descent(f, dfs, e, stepx):
    n = len(dfs)
    M = [0] * n
    gradf = grad(*dfs)
    # print(*inspect.getsource(gradf))
    x = M
    i = 0
    dx = 0
    ff = 0
    while True:
        prevff = ff
        ff = f(*x)
        prevdx = dx
        dx = gradf(*x)
        clog(f'x{i} = {x}, dx = {dx}')
        clog(f'prevdx = {prevdx}, dx = {dx}')
        clog(vector_abs(*dx))
        print('f', ff - prevff)
        if vector_abs(*dx) <= e:
            return x
        x = [(x[i] - stepx * dx[i]) for i in range(n)]
        i += 1
