import time
from math import sqrt

from asymptotics import coefficients, main_term
from triples import a268756
from verify import by_sieve


def timed(f, *args):
    t = time.perf_counter()
    v = f(*args)
    return time.perf_counter() - t, v


def bench_linear():
    print("table 1: sieve O(n) against the formula")
    print("n, sieve, formula")
    for e in range(4, 8):
        n = 10**e
        ts, vs = timed(lambda m: by_sieve(m)[0], n)
        tf, vf = timed(a268756, n)
        assert vs == vf
        print(n, "%.4f" % ts, "%.4f" % tf)


def bench_large():
    print("table 2: large n")
    print("n, time, a(n), (a(n) - main term) / sqrt(n)")
    for e in range(8, 14):
        n = 10**e
        t, v = timed(a268756, n)
        print(n, "%.3f" % t, v, "%.4f" % ((v - main_term(n)) / sqrt(n)), flush=True)


if __name__ == "__main__":
    print("coefficients c2, c1, c0:", *coefficients())
    bench_linear()
    bench_large()
