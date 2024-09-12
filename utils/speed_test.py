import time


def speed_test(func, repeats=1_000_000):
    t0 = time.time()
    for i in range(repeats):
        func()
    t1 = time.time()
    total = t1 - t0
    print(f'{total} seconds')
