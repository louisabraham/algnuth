"""
This module provides functions to manipulate
extension fields given their minimal polynomial.
"""

from math import pi, factorial

from .polynom import Polynomial
from .jacobi import sieve


def minkowski_bound(P):
    """
    Any ideal of the ring of integers
    of the algebraic number field whose
    minimal polynomial is P contains
    an integer N such that
    1 ≤ N ≤ minkowski_bound(P)
    """
    return (4 / pi) ** P.r2 * factorial(P.deg) / P.deg ** P.deg * abs(P.disc) ** .5


def idealsContaining(P, p):
    """
    Ideals of the extension field of minimal
    polynomial P containing the prime p
    """
    Pmodp = P.reduceP(p)
    c, Ds = Pmodp.factor()
    print('%s mod %s = %s' % (P, p, Polynomial.ppfactors((c, Ds))))
    print("(%s) = " % p +
          '⋅'.join(("(%s, %s)" % (p, D)
                    + (v > 1) * ("^%s" % v))
                   if sum(Ds.values()) > 1 else "(%s)" % p
                   for D, v in Ds.items()).replace("X", "α"))


def factorIdeals(P):
    """
    Finds the ideals of the ring of integers
    of the algebraic number field whose
    minimal polynomial is P
    """
    b = int(minkowski_bound(P))
    if b == 1:
        print('Principal!')
    for p in sieve(b + 1):
        idealsContaining(P, p)
    print()
