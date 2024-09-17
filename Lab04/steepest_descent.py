from utils.grad import grad, vector_abs, normalize


def steepest_descent(f, dfs, e):
    n = len(dfs)
    M = [0] * n
    gradf = grad(*dfs)
    x = M
    while True:
        dx = gradf(*x)
        if vector_abs(*dx) <= e:
            return x
        dx = normalize(dx)
        print(dx)
        
        # Need to count stepx
        # expr = sum([exp(x[i] - h * dx[i]) for i in range(n)])
        # print(expr)
        # df = diff(expr, h)
        # df
        # print(d)
        # input()
        h_coef = sum(dx)
        coef = sum(x)
        h = coef / h_coef
        x = [(x[i] - h * dx[i]) for i in range(n)]
