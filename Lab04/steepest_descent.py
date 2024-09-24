from utils.grad import grad
from utils.log import clog
from utils.vector import coef_multiply, vector_abs, normalize, scalar_multiply, sum_vector
from Lab02.bisection_method import bisection_method


def steepest_descent(f, dfs, e):
    n = len(dfs)
    M = [0] * n
    gradf = grad(*dfs)
    cur_x = M
    while True:
        dx = gradf(*cur_x)
        if vector_abs(*dx) <= e:
            return cur_x
        dx = normalize(dx)
        clog(dx)

        xp = bisection_method(lambda x: f(*sum_vector(cur_x, coef_multiply(x, dx))), -10, 10, e, verbose=False)
        cur_x = sum_vector(cur_x, coef_multiply(xp, dx))
