![travis](https://travis-ci.org/louisabraham/algnuth.svg?branch=master)

Algebraic Number Theory package
===============================

**Louis Abraham** and **Yassir Akram**

Installation
------------

    pip install --upgrade algnuth

or get the development version with:

    pip install --upgrade git+https://github.com/louisabraham/algnuth

Features
--------

### Jacobi symbol

``` pycon
>>> from algnuth.jacobi import jacobi
>>> jacobi(3763, 20353)
-1
```

### Solovay-Strassen primality test

``` pycon
>>> from algnuth.jacobi import solovay_strassen
>>> p = 12779877140635552275193974526927174906313992988726945426212616053383820179306398832891367199026816638983953765799977121840616466620283861630627224899026453
>>> q = 12779877140635552275193974526927174906313992988726945426212616053383820179306398832891367199026816638983953765799977121840616466620283861630627224899027521
>>> n = p * q
>>> solovay_strassen(p)
True
>>> solovay_strassen(q)
True
>>> solovay_strassen(n)
False
```

### Quadratic forms

``` pycon
>>> from algnuth.quadratic import *
>>> display_classes(-44)
x^2 + 11⋅y^2
2⋅x^2 + 2⋅xy + 6⋅y^2
3⋅x^2 - 2⋅xy + 4⋅y^2
3⋅x^2 + 2⋅xy + 4⋅y^2
>>> display_primitive_forms(-44)
x^2 + 11⋅y^2
3⋅x^2 - 2⋅xy + 4⋅y^2
3⋅x^2 + 2⋅xy + 4⋅y^2
>>> display_ambiguous_classes(-44)
x^2 + 11⋅y^2
2⋅x^2 + 2⋅xy + 6⋅y^2
>>> display(*reduced(18, -10, 2))
2⋅x^2 + 2⋅xy + 6⋅y^2
```

### Real polynomials

``` pycon
>>> from algnuth.polynom import Polynomial
>>> P = Polynomial([0] * 10 + [-1, 0, 1])
>>> print(P)
X^12-X^10
>>> P(2)
3072
>>> P.disc
0
>>> P.sturm() # Number of distinct real roots
3
>>> P.r1 # Number of real roots with multiplicity
12
```

### Modular arithmetic

``` pycon
>>> P = Polynomial([1, 2, 3])
>>> Pmodp = P % 41
>>> print(Pmodp ** 3)
27⋅X^6+13⋅X^5+22⋅X^4+3⋅X^3+21⋅X^2+6⋅X+1
>>> print((P ** 3) % 41)
27⋅X^6+13⋅X^5+22⋅X^4+3⋅X^3+21⋅X^2+6⋅X+1
```

### Polynomial division

``` pycon
>>> A = Polynomial([1, 2, 3, 4]) % 7
>>> B = Polynomial([0, 1, 2]) % 7
>>> print(A)
4⋅X^3+3⋅X^2+2⋅X+1
>>> print(B)
2⋅X^2+X
>>> print(A % B)
5⋅X+1
>>> print(A // B)
2⋅X+4
>>> print((A // B) * B + A % B)
4⋅X^3+3⋅X^2+2⋅X+1
```

### Berlekamp's factorization algorithm

``` pycon
>>> P = Polynomial([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
>>> Pmodp = P % 41
>>> print(Polynomial.ppfactors(Pmodp.factor()))
12⋅(X+31)⋅X⋅(X^2+40⋅X+24)⋅(X^2+36⋅X+13)⋅(X^6+34⋅X^5+26⋅X^4+13⋅X^3+25⋅X^2+26⋅X+35)
```

### Unique Factorization of Ideals

``` pycon
>>> from algnuth.ideals import factorIdeals
>>> factorIdeals(Polynomial([4, 0, 0, 1]))
X^3+4 mod 2 = X^3
(2) = (2, α)^3
X^3+4 mod 3 = (X+1)^3
(3) = (3, α+1)^3
X^3+4 mod 5 = (X+4)⋅(X^2+X+1)
(5) = (5, α+4)⋅(5, α^2+α+1)
```
