import random
from math import gcd, isqrt

import numpy as np

from divisors import divisor_prefix
from triples import a061201, a268732, a268756

DATA = [
    1, 5, 9, 17, 21, 35, 39, 53, 61, 75, 79, 107, 111, 125, 139, 160, 164, 192, 196,
    224, 238, 252, 256, 304, 312, 326, 340, 368, 372, 418, 422, 452, 466, 480, 494,
    550, 554, 568, 582, 630, 634, 680, 684, 712, 740, 754, 758, 830, 838, 866, 880,
    908, 912, 960, 974,
]
BFILE = {
    100: 2313, 200: 5977, 300: 10282, 400: 15024, 500: 20000, 600: 25530, 700: 31011,
    800: 36931, 900: 43003, 1000: 49027, 2000: 117970, 3000: 195821, 4000: 279567,
    5000: 368030, 6000: 460344, 7000: 555583, 8000: 653955, 9000: 754879, 10000: 857678,
}


def by_definition(n):
    total = 0
    for x in range(1, n + 1):
        for y in range(1, n // x + 1):
            xy = x * y
            for r in range(1, xy + 1):
                if xy % r == 0 and (x % r == 0 or y % r == 0):
                    total += 1
    return total


def by_sieve(n):
    prefix = divisor_prefix(n + 2)
    d = np.diff(prefix, prepend=0)
    x = np.arange(1, n + 1, dtype=np.int64)
    cubic = int((d[1:n + 1] * (n // x)).sum())
    e = np.arange(1, isqrt(n) + 1, dtype=np.int64)
    square = int(prefix[n // (e * e)].sum())
    return 2 * cubic - square, cubic, square


def check_data():
    assert [a268756(n) for n in range(1, len(DATA) + 1)] == DATA
    for n, v in BFILE.items():
        assert a268756(n) == v, n
    print("formula agrees with the %d terms of A268756 and with %d values of the b-file up to n = 10000" % (len(DATA), len(BFILE)))


def check_definition():
    for n in range(1, 101):
        assert a268756(n) == by_definition(n), n
    print("formula equals the definition (triples x, y, r) for n = 1..100")


def check_parts():
    assert [a268732(n) for n in range(1, 13)] == [1, 3, 5, 9, 11, 15, 17, 23, 27, 31, 33, 41]
    assert [a061201(n) for n in range(1, 13)] == [1, 4, 7, 13, 16, 25, 28, 38, 44, 53, 56, 74]
    print("the two parts equal A268732 and A061201 for n = 1..12")


def check_sieve():
    random.seed(268756)
    cases = list(range(1, 2001)) + [10**e + d for e in range(3, 8) for d in (0, 1)]
    cases += [random.randrange(2000, 10**7) for _ in range(60)]
    for n in cases:
        v, cubic, square = by_sieve(n)
        assert a268756(n) == v, n
        assert a061201(n) == cubic and a268732(n) == square, n
    print("formula equals the sieve sum for n = 1..2000 and %d further n up to 10^7" % (len(cases) - 2000))
    for n in [random.randrange(10**5, 10**7) for _ in range(30)]:
        assert a268756(n, B=isqrt(n) + 2) == by_sieve(n)[0], n
    print("the direct branch (table of size sqrt(n)) agrees for 30 random n up to 10^7")


if __name__ == "__main__":
    check_data()
    check_definition()
    check_parts()
    check_sieve()
    print("all checks passed")
