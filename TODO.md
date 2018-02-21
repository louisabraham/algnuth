Pseudoprimality tests
=====================

-   [Miller-Rabin](https://en.wikipedia.org/wiki/Miller–Rabin_primality_test)
-   [Fermat](https://en.wikipedia.org/wiki/Fermat_pseudoprime)
-   [Lucas](https://en.wikipedia.org/wiki/Lucas_pseudoprime)
-   [Baillie-PSW](https://en.wikipedia.org/wiki/Baillie%E2%80%93PSW_primality_test)
-   Deterministic variants of Miller-Rabin

Elliptic curves
===============

-   Weierstrass form
-   Montgomery form
-   Generic class for other int implementations
-   For Montgomery: PRAC and safe Ladder

gmpy2 support
=============

-   [gmpy2](https://github.com/aleaxit/gmpy) support for elliptic curves
-   implement alternative faster sieves using
    [gmpy2](https://gmpy2.readthedocs.io/en/latest/advmpz.html) or numpy
-   interface the [Advanced Number Theory Functions from
    gmpy2](https://gmpy2.readthedocs.io/en/latest/advmpz.html#advanced-number-theory-functions)
    and replicate them in pure Python for compatibility

Factorization algorithms
========================

-   Lenstra's algorithm on elliptic curves
-   Multiple-polynomial quadratic sieve
-   Parallelism with
    [SCOOP](https://scoop.readthedocs.io/en/0.7/api.html?highlight=futures#scoop.futures.as_completed)
-   Hart's one line factoring algorithm
    ([pdf](http://wrap.warwick.ac.uk/54707/1/WRAP_Hart_S1446788712000146a.pdf))
-   Other algorithms from
    [primefac](https://pypi.python.org/pypi/primefac)

Maybe
=====

-   Multiprocessing support: better than SCOOP locally and because of
    the ability to terminate
