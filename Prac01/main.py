from Prac01.bisection_method import bisection_method
from Prac01.f import a, b, e, f, fd, fdd, round_digits
from Prac01.fibonacci import fibonacci_minimization
from Prac01.golden_ratio_method import golden_ratio_method
from Prac01.newton_method import newton_method
from Prac01.secant_method import secant_method
import inspect


def main():
    print(f"f = {inspect.getsource(f)}")
    print(f"[{a}:{b}], e = {e}")
    print("====")
    print("Половинного деления")
    res = bisection_method(f, a, b, e)
    print(round(res, round_digits))
    print("====")
    print("Золотого сечения")
    res = golden_ratio_method(f, a, b, e)
    print(round(res, round_digits))
    print("====")
    print("Фибоначчи")
    res = fibonacci_minimization(f, a, b, e)
    print(round(res, round_digits))
    print("====")
    print("Метод хорд")
    res = secant_method(f, fd, a, b, e)
    print(round(res, round_digits))
    print("====")
    print("Метод Ньютона")
    res = newton_method(f, fd, fdd, a, b, e)
    print(round(res, round_digits))


if __name__ == "__main__":
    main()
