import inspect

from Lab04.f import f, dfx1, dfx2, dfx3, e, dx, round_digits

from Lab04.gradient_descent import gradient_descent
from Lab04.steepest_descent import steepest_descent
from utils.func import invert, invert_func


def main():
    print(f"f = {inspect.getsource(f)}")
    print("====")
    print("Градиентный спуск")
    print("Минимум")
    res = gradient_descent(f, [dfx1, dfx2, dfx3], e, dx)
    print(*[round(i, round_digits) for i in res], sep=", ")
    # print("Максимум")
    # res = invert(gradient_descent(invert_func(f), [invert_func(dfx1), invert_func(dfx2), invert_func(dfx3)], e, dx))
    # print(*[round(i, round_digits) for i in res], sep=', ')

    print("Наискорейший спуск")
    print("Минимум")
    res = steepest_descent(f, [dfx1, dfx2, dfx3], e)
    print(*[round(i, round_digits) for i in res], sep=", ")
    # print("Максимум")
    # res = invert(steepest_descent(invert_func(f), [invert_func(dfx1), invert_func(dfx2), invert_func(dfx3)], e))
    # print(*[round(i, round_digits) for i in res], sep=', ')


if __name__ == "__main__":
    main()
