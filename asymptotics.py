from math import log

from mpmath import euler, mp, stieltjes, zeta

mp.dps = 30


def coefficients():
    g = euler
    g1 = stieltjes(1)
    z2 = zeta(2)
    dz2 = zeta(2, derivative=1)
    c2 = 1
    c1 = 6 * g - 2 - z2
    c0 = 6 * g * g - 6 * g + 2 - 6 * g1 - z2 * (2 * g - 1) - 2 * dz2
    return float(c2), float(c1), float(c0)


def main_term(n):
    c2, c1, c0 = coefficients()
    L = log(n)
    return n * (c2 * L * L + c1 * L + c0)
