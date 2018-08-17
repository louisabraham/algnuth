"""
Jacobi symbol, Solovay–Strassen primality test and sieve of Eratosthenes
"""

from random import randrange
from math import gcd


def expsign(sign, exp):
    """
    optimization of sign ** exp
    """
    if sign == 1:
        return 1
    assert sign == -1
    return -1 if exp % 2 else 1


def jacobi(m, n):
    """
    Jacobi's symbol
    the rule for (-1/n) is not used
    """
    assert n % 2
    if m == 2:
        if n % 8 in [1, 7]:
            return 1
        return -1
    m %= n
    q = 0
    while m & 1 == 0:
        m >>= 1
        q += 1
    if m == 1:
        return expsign(jacobi(2, n), q)
    return (expsign(jacobi(2, n), q)
            * (-1 if (n % 4 == 3) and (m % 4 == 3) else 1)
            * jacobi(n, m))


def solovay_strassen(n, prec=50):
    """
    Solovay–Strassen primality test
    with error probability less than 2^-prec
    """
    if n == 1:
        return False
    if n % 2 == 0:
        return n == 2
    e = (n - 1) // 2
    for _ in range(prec):
        x = randrange(1, n)
        if gcd(x, n) != 1 or pow(x, e, n) != (jacobi(x, n) % n):
            return False
    return True


def sieve(n):
    """
    Sieve of Eratosthenes
    sieve(n) -> list of primes in range(n)
    """
    n -= 1
    # l[i] = True iff i is prime
    # ignore the first two values
    l = [True] * (n + 1)
    for x in range(2, round(n**.5) + 1):
        # all factors are ≤ int(n**.5)
        # round is there in case of float error
        if l[x]:
            # there are exactly (n // x - 1)
            # multiples of x greater than x
            l[2 * x::x] = [False] * (n // x - 1)
    return [i for i in range(2, n + 1) if l[i]]


def isprimerm(n, l=[2, 325, 9375, 28178, 450775, 9780504, 1795265022]):
    """
    Miller–Rabin primality test
    """
    if n == 1:
        return False
    if n in l:
        return True
    if n % 2 == 0:
        return False
    b = 0
    for a in l:
        if pow(a, n - 1, n) != 1:
            return False
        if b == 0 or pow(a, b, n) != 1:
            r = 1
            b = n - 1
            while b % 2 == 0 and r == 1:
                r = pow(a, b, n)
                b = b // 2
            if r != 1 and r != n - 1:
                return False
    return True


def test_solovay_strassen(limit=10**5):
    """
    Runs in ~20s with limit = 10^5
    """
    primes = set(sieve(limit))
    for i in range(limit):
        assert (i in primes) == solovay_strassen(i)


if __name__ == '__main__':
    test_solovay_strassen(10**3)
    p = 12779877140635552275193974526927174906313992988726945426212616053383820179306398832891367199026816638983953765799977121840616466620283861630627224899026453
    q = 12779877140635552275193974526927174906313992988726945426212616053383820179306398832891367199026816638983953765799977121840616466620283861630627224899027521
    n = p * q
    assert solovay_strassen(p)
    assert solovay_strassen(q)
    assert not solovay_strassen(n)
