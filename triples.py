from math import isqrt

import numpy as np

from divisors import LIMIT, divisor_prefix, divisor_sums


def table_size(n):
    return max(isqrt(n) + 2, min(int(n ** (2 / 3)), LIMIT))


def square_part(n, table, B):
    e = np.arange(1, isqrt(n) + 1, dtype=np.int64)
    return int(divisor_sums(n // (e * e), table, B).sum())


def cubic_sum(n, table, B):
    s = isqrt(n)
    c = np.arange(1, s + 1, dtype=np.int64)
    total = int(divisor_sums(n // c, table, B).sum())
    q = np.arange(1, n // (s + 1) + 1, dtype=np.int64)
    counts = n // q - np.maximum(n // (q + 1), s)
    counts = np.maximum(counts, 0)
    return total + int((table[q] * counts).sum())


def a268756(n, B=None):
    B = B or table_size(n)
    table = divisor_prefix(B)
    return 2 * cubic_sum(n, table, B) - square_part(n, table, B)


def a268732(n):
    B = table_size(n)
    return square_part(n, divisor_prefix(B), B)


def a061201(n):
    B = table_size(n)
    return cubic_sum(n, divisor_prefix(B), B)
