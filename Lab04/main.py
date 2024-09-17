import inspect

from Lab04.f import f, dfx1, dfx2, dfx3, e, dx, round_digits

from Lab04.gradient_descent import gradient_descent
from Lab04.steepest_descent import steepest_descent


def main():
    print(f"f = {inspect.getsource(f)}")
    print("====")
    print("Градиентный спуск")
    res = gradient_descent(f, [dfx1, dfx2, dfx3], e, dx)
    print(*[round(i, round_digits) for i in res], sep=', ')
    # print("Наискорейший спуск")
    # res = steepest_descent(f, [dfx1, dfx2, dfx3], e)
    # print(round(res, round_digits))


if __name__ == "__main__":
    main()
