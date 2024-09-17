import inspect

from Lab03.f import a, b, dx, efx, ex, f, fd, round_digits, x1
from Lab03.square_interpolation import square_interpolation


def main():
    print(f"f = {inspect.getsource(f)}")
    print(f"[{a}:{b}], e1 = {ex}, e2 = {efx}")
    print("====")
    print("Квадратная аппроксимация")
    res = square_interpolation(f, fd, a, b, ex, efx, x1, dx)
    print(round(res, round_digits))


if __name__ == "__main__":
    main()
