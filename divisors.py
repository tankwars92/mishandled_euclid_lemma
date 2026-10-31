from math import isqrt

import numpy as np

LIMIT = 2 * 10**7


def divisor_prefix(B):
    d = np.zeros(B + 1, dtype=np.int32)
    for k in range(1, isqrt(B) + 1):
        d[k * k] += 1
        d[k * (k + 1)::k] += 2
    return np.cumsum(d, dtype=np.int64)


def divisor_sum_direct(x):
    s = isqrt(x)
    k = np.arange(1, s + 1, dtype=np.int64)
    return 2 * int((x // k).sum()) - s * s


def divisor_sums(values, table, B):
    values = np.asarray(values, dtype=np.int64)
    out = np.empty(values.shape, dtype=np.int64)
    small = values <= B
    out[small] = table[values[small]]
    for i in np.nonzero(~small)[0]:
        out[i] = divisor_sum_direct(int(values[i]))
    return out
