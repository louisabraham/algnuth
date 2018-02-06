"""
Modular arithmetic
"""


class ModInt:

    """
    Integers of Z/pZ
    """

    def __init__(self, a, n):
        self.v = a % n
        self.n = n

    def __eq__(a, b):
        if isinstance(b, ModInt):
            return not bool(a - b)
        else:
            return NotImplemented

    def __hash__(self):
        return hash((self.v, self.n))

    def __bool__(self):
        return bool(self.v)

    def __add__(a, b):
        assert isinstance(b, ModInt)
        assert a.n == b.n
        return ModInt(a.v + b.v, a.n)

    def __radd__(a, b):
        assert isinstance(b, int)
        return ModInt(a.v + b, a.n)

    def __neg__(a): return ModInt(-a.v, a.n)

    def __sub__(a, b): return ModInt(a.v - b.v, a.n)

    def __mul__(a, b):
        if isinstance(b, int):
            return ModInt(b * a.v, a.n)
        elif isinstance(b, ModInt):
            assert a.n == b.n
            return ModInt(a.v * b.v, a.n)
        return NotImplemented

    def __rmul__(a, b):
        return a * b

    def __pow__(P, k):
        assert isinstance(k, int)
        V = 1
        A = P
        while k:
            if k & 1:
                V *= A
            k >>= 1
            if not k:
                break
            A *= A
        return V

    def __truediv__(a, b):
        assert isinstance(b, ModInt)
        assert a.n == b.n
        return ModInt(
            a.v * ModInt.extended_euclid(b.v, b.n)[0], a.n)

    def __rtruediv__(a, k):
        assert isinstance(k, int)
        return ModInt(k, a.n) / a

    @staticmethod
    def extended_euclid(a, b):
        up, vp = (1 if a >= 0 else -1), 0
        u, v = 0, (1 if b >= 0 else -1)
        rp, r = a * up, b * v
        while r:
            rr = rp // r
            rp -= rr * r
            up -= rr * u
            vp -= rr * v
            rp, r = r, rp
            up, u = u, up
            vp, v = v, vp
        return up, vp

    def __repr__(self):
        return '%s(%s, %s)' % (self.__class__.__name__, self.v, self.n)

    def __str__(self):
        return '%s' % self.v


from collections import defaultdict
import numpy as np


class Polynomial:

    """
    Generic class for polynomials
    Works with int, float and ModInt
    """

    def __len__(self):
        return len(self.C)

    def trim(C):
        i = len(C) - 1
        while i >= 0 and not C[i]:
            i -= 1
        return C[:i + 1]

    def __init__(self, C=None):
        if C is None:
            C = []
        self.C = Polynomial.trim(C)

    @property
    def deg(self):
        return len(self.C) - 1

    def prime(self): return Polynomial([i * self[i]
                                        for i in range(1, len(self))])

    def eval(self, x):
        if not self:
            return 0
        v = self[-1]
        for c in self[-2::-1]:
            v = v * x + c
        return v

    def shift(self, d): return Polynomial(
        [0 * self[0]] * d + self.C if self else [])

    def __eq__(P, Q):
        return P.deg == Q.deg and all(cP == cQ for cP, cQ in zip(P, Q))

    def __hash__(self):
        return hash(tuple(self.C))

    def __call__(self, x): return Polynomial.eval(self, x)

    def __getitem__(self, x): return self.C[x]

    def __neg__(P): return Polynomial([-c for c in P.C])

    def __add__(P, Q):
        if len(P.C) < len(Q.C):
            P, Q = Q, P
        return Polynomial([P[d] + Q[d] for d in range(len(Q))] + P[len(Q):])

    def __sub__(P, Q): return P + (-Q)

    def _mulpoly(P, Q):
        assert isinstance(Q, Polynomial)
        return Polynomial([sum(P[k] * Q[d - k]
                               for k in range(max(0, d + 1 - len(Q)),
                                              min(d + 1, len(P)))
                               ) for d in range(len(P) + len(Q) - 1)])

    def _mulscal(P, k):
        return Polynomial([k * c for c in P])

    def __mul__(P, Q):
        if isinstance(Q, Polynomial):
            return P._mulpoly(Q)
        return P._mulscal(Q)

    def __rmul__(P, Q):
        return P * Q

    def __pow__(P, k):
        assert isinstance(k, int)
        V = 1
        A = P
        while k:
            if k & 1:
                V *= A
            k >>= 1
            if not k:
                break
            A *= A
        return V

    def __iter__(self):
        yield from self.C

    def euclidean_division(A, B):
        Q = [0 * B[0]] * max(0, len(A) - len(B) + 1)
        while len(A.C) >= len(B.C):
            Q[len(A.C) - len(B.C)] = A[-1] / B[-1]
            A -= B.shift(len(A) - len(B)) * (A[-1] / B[-1])
        return Polynomial(Q), A

    def __floordiv__(A, B):
        assert isinstance(B, Polynomial)
        return A.euclidean_division(B)[0]

    def __mod__(A, B):
        """
        Polynomial euclidian division
        or modular reduction
        """
        if isinstance(B, Polynomial):
            return A.euclidean_division(B)[1]
        else:
            assert isinstance(B, int)
            assert all(isinstance(c, int) for c in A)
            return A.reduceP(B)

    def __lt__(A, B): return A.deg < B.deg

    def __bool__(self): return bool(self.C)

    def gcd(A, B):
        while B:
            A, B = B, A % B
        return A * (1 / A[-1])

    @staticmethod
    def gaussianElimKer(M, zero, one):
        """
        Outputs an element of the kernel of M
        zero and one are elements of the same field
        """
        # V satisfies the invariant
        # M = V M_0
        V = [Polynomial([zero] * i + [one]) for i in range(len(M))]
        pivots = [None] * (len(M) + 1)
        for l in range(len(M)):
            while M[l].deg >= 0:
                idp = M[l].deg
                if pivots[idp] == None:
                    pivots[idp] = l
                    break
                else:
                    c = M[l][idp] / M[pivots[idp]][idp]
                    M[l] -= c * M[pivots[idp]]
                    V[l] -= c * V[pivots[idp]]
            else:
                # If a line is null, we found an element of the kernel
                return V[l]
        return None

    def computeQ(P):
        # only for Z/pZ[X] square-free polynoms, for p prime
        p = P[0].n
        # We ignore the image of 1 because (F-Id)(1) = 0
        M = [Polynomial(([ModInt(0, p)] * (i * p)) + [ModInt(1, p)]) % P
             for i in range(1, P.deg)]
        # M -= Id
        for i in range(1, P.deg):
            M[i - 1] -= Polynomial([ModInt(0, p)] * i + [ModInt(1, p)])
        # We find an element of the kernel by Gaussian elimination
        pQ = Polynomial.gaussianElimKer(M, ModInt(0, p), ModInt(1, p))
        # We put back the 1 tha was removed
        return pQ.shift(1) if pQ is not None else None

    def factor_unit(P):
        """
        Berlekamp's algorithm
        only in Z/pZ
        """
        assert all(isinstance(c, ModInt) for c in P)
        assert len(set(c.n for c in P)) == 1
        if P.deg == 1:
            return defaultdict(int, {P: 1})

        p = P[0].n

        S = Polynomial.gcd(P, P.prime())
        if S.deg == P.deg:
            # P' = 0 so P = R^p
            R = Polynomial(P.C[::p])
            return defaultdict(int,
                               {D: p * v
                                for D, v in Polynomial.factor_unit(R).items()})
        else:
            factors = defaultdict(int)
            if S.deg:
                for D, v in S.factor_unit().items():
                    factors[D] += v
                P //= S
            # P is now square-free
            # We look for Q in Ker(F-Id) \ {1}
            Q = Polynomial.computeQ(P)
            if Q is None:
                # P is irreducible
                factors[P] += 1
            else:
                # P is the product of the gcd(P, Q-i)
                # that are factored recursively
                for i in range(p):
                    D = Polynomial.gcd(P, Q - Polynomial([ModInt(i, p)]))
                    if D.deg:
                        for DD, v in D.factor_unit().items():
                            factors[DD] += v
            return factors

    def factor(P):
        """
        Factorization of P
        only in Z/pZ
        """
        cd = P[-1]
        p = cd.n
        if P.deg == 0:
            return (cd, defaultdict(int))
        P = P * (1 / cd)
        return (cd, Polynomial.factor_unit(P))

    @staticmethod
    def ppfactors(fz):
        c, Ds = fz
        a = str(c) if not Ds or c * c != c else ''
        l = [a] + [(str(D) if D.deg == 1 and not D[0] else ('(%s)' % D))
                   + (v > 1) * ('^%s' % v)
                   for D, v in sorted(Ds.items(),
                                      key=lambda e: (e[0].deg, e[1]))]
        return '⋅'.join(i for i in l if i)

    def reduceP(P, p):
        return Polynomial([ModInt(c, p) for c in P])

    @staticmethod
    def sign_changes(l):
        return sum(a * b < 0 for a, b in zip(l, l[1:]))

    def isreal(P):
        return not any(isinstance(c, ModInt) for c in P)

    def isinteger(P):
        return all(isinstance(c, int) for c in P)

    def sturm(P):
        """
        Number of distinct real roots
        by Sturm's theorem.
        Only works on int or float coefficients
        """
        inf = float('inf')
        assert P.isreal()
        A = P
        B = A.prime()
        l1 = [A(-inf)]
        l2 = [A(inf)]
        while B:
            l1.append(B(-inf))
            l2.append(B(inf))
            B, A = -A % B, B
        return Polynomial.sign_changes(l1) - Polynomial.sign_changes(l2)

    @property
    def r1(P):
        """
        Number of real roots with multiplicity
        """
        assert P.isreal()
        ans = 0
        s = P.sturm()
        while s:
            ans += s
            P = P.gcd(P.prime())
            s = P.sturm()
        return ans

    @property
    def r2(P):
        ans = P.deg - P.r1
        assert ans % 2 == 0
        return ans // 2

    def sylvester(P, Q):
        """
        Sylvester's matrix
        """
        assert P.isreal()
        assert Q.isreal()
        p = P.deg
        q = Q.deg
        P = np.array(P)
        Q = np.array(Q)
        m = np.zeros((p + q, p + q))
        for i in range(q):
            m[i][i:i + p + 1] = P
        for i in range(p):
            m[q + i][i:i + q + 1] = Q
        return m

    def resultant(P, Q):
        """
        Resultant of two real polynomials
        """
        return np.linalg.det(P.sylvester(Q))

    @property
    def disc(P):
        """
        Discriminant of a real polynomial
        """
        ans = P.resultant(P.prime()) / P[-1]
        if P.isinteger():
            ans = int(ans.round())
        if P.deg % 4 in [0, 1]:
            return ans
        else:
            return -ans

    def __repr__(self):
        return '%s(%s)' % (self.__class__.__name__, self.C)

    @staticmethod
    def _formatmonomial(c, d):
        assert c
        a = b = ''
        if c * c != c or not d:
            a = str(c) + (d != 0) * '⋅'
        if d > 1:
            b = 'X^' + str(d)
        elif d == 1:
            b = 'X'
        return a + b

    def __str__(self):
        if not self.C:
            return "0"
        ans = '+'.join(self._formatmonomial(c, d)
                       for (d, c) in reversed(list(enumerate(self))) if c)
        return ans.replace("+-", "-").replace('-1⋅', '-')
