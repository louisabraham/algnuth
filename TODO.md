Pseudoprimality tests
=====================

-   [Miller-Rabin](https://en.wikipedia.org/wiki/Miller–Rabin_primality_test)
-   [Fermat](https://en.wikipedia.org/wiki/Fermat_pseudoprime)
-   [Lucas](https://en.wikipedia.org/wiki/Lucas_pseudoprime)
-   [Baillie-PSW](https://en.wikipedia.org/wiki/Baillie%E2%80%93PSW_primality_test)
-   Deterministic variants of Miller-Rabin

Elliptic curves
===============

-   [Weierstrass form](https://github.com/pkruk/pylenstra)
-   Montgomery form
-   Generic class for other int implementations
-   For Montgomery: [PRAC and safe
    Ladder](https://arxiv.org/pdf/1703.01863.pdf)
-   Add other curves and formulas from the [Explicit-Formulas
    Database](https://hyperelliptic.org/EFD/)?

Other references:
-----------------

-   <https://wstein.org/edu/124/lenstra/lenstra.pdf>
-   <https://wstein.org/edu/124/misc/montgomery.pdf>
-   <https://wstein.org/edu/124/misc/arjen_lenstra_factoring.pdf>
-   <https://wstein.org/edu/124/misc/koblitz_ecc.pdf>

gmpy2 support
=============

-   [gmpy2](https://github.com/aleaxit/gmpy) support for elliptic curves
-   implement alternative faster sieves using
    [gmpy2](https://gmpy2.readthedocs.io/en/latest/advmpz.html) or
    [numpy](https://stackoverflow.com/a/3035188/5133167)
-   interface the [Advanced Number Theory Functions from
    gmpy2](https://gmpy2.readthedocs.io/en/latest/advmpz.html#advanced-number-theory-functions)
    and replicate them in pure Python for compatibility

Factorization algorithms
========================

-   [Lenstra's
    algorithm](https://wstein.org/edu/124/lenstra/lenstra.pdf) on
    elliptic curves
-   [Multiple polynomial quadratic
    sieve](https://codegolf.stackexchange.com/a/9088/47040)
-   Parallelism with
    [SCOOP](https://scoop.readthedocs.io/en/0.7/api.html?highlight=futures#scoop.futures.as_completed)
-   Hart's one line factoring algorithm
    ([pdf](http://wrap.warwick.ac.uk/54707/1/WRAP_Hart_S1446788712000146a.pdf))
-   Other algorithms from
    [primefac](https://pypi.python.org/pypi/primefac)

Other algorithms
================

-   Modular square root: Tonelli--Shanks and Cipolla's algorithms
-   Algorithms from [E. Bach, J.O. Shallit *Algorithmic Number Theory:
    Efficient algorithms* MIT
    Press, (1996)](https://mitpress.mit.edu/books/algorithmic-number-theory)

Maybe
=====

-   Multiprocessing support: better than SCOOP locally and because of
    the ability to terminate
-   [General number field
    sieve](https://wstein.org/129/references/Lenstra-Lenstra-Manasse-Pollard-The%20number%20field%20sieve.pdf),
    see also <https://github.com/radii/msieve>
