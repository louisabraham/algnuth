"""
Basic functions on quadratic forms
"""

from math import sqrt, ceil, gcd

from functools import reduce, partial
gcdl = partial(reduce, gcd)


def Cl(D):
    """
    List of classes of discriminant D
    """
    assert D < 0
    assert D % 4 in [0, 1]
    l = []
    for a in range(1, int(sqrt(-D / 3)) + 1):
        for b in range(-a, a + 1):
            if (b**2 - D) % (4 * a) == 0:
                c = (b**2 - D) // (4 * a)
                if c >= a:
                    if b >= 0 or (abs(b) != a and a != c):
                        l.append((a, b, c))
    return l


def Prim(D):
    """
    List of primitive forms of discriminant D
    """
    return [i for i in Cl(D) if gcdl(i) == 1]


def display(a, b, c):
    """
    Displays a form
    """
    if a == b == c == 0:
        print(0)
    ans = ''
    if a:
        if a < 0:
            ans += ' - '
        ans += (abs(a) != 1) * str(abs(a)) + "x^2"
    if b:
        if b > 0:
            ans += ' + '
        elif b < 0:
            ans += ' - '
        ans += (abs(b) != 1) * str(abs(b)) + "xy"
    if c:
        if c > 0:
            ans += ' + '
        elif c < 0:
            ans += ' - '
        ans += (abs(c) != 1) * str(abs(c)) + "y^2"
    print(ans)


def reduced(a, b, c):
    """
    Reduced form
    """
    while not -abs(a) < b <= abs(a) <= abs(c):
        if abs(c) < abs(a):
            a, b, c = c, -b, a
        elif abs(c) >= abs(a) and abs(b) >= abs(a):
            sign = 1 if abs(b + a) < abs(b) else -1
            b, c = b + sign * 2 * a, c + a + sign * b
    return a, b, c


def display_classes(D):
    for i in Cl(D):
        display(*i)


def display_primitive_forms(D):
    for i in Prim(D):
        display(*i)


def h(D):
    """
    Number of primitive forms of discriminant D
    """
    return len(Prim(D))


def is_ambiguous(a, b, c):
    return b == 0 or b == a or c == a


def ambiguous_classes(D):
    return [i for i in Cl(D) if is_ambiguous(*i)]


def display_ambiguous_classes(D):
    for i in ambiguous_classes(D):
        display(*i)


def a(D):
    """
    Number of ambiguous classes
    """
    return len(ambiguous_classes(D))


def func(a, b, c):
    """
    Transforms a triple into a function
    """
    return lambda x, y: a * x * x + b * x * y + c * y * y


def genus(a, b, c):
    f = func(a, b, c)
    D = -(b**2 - 4 * a * c)
    return tuple(sorted(set(f(x, y) % D for x in range(D) for y in range(D) if gcd(f(x, y), D) == 1)))


def genera(D):
    l = Prim(D)
    s = set()
    for t in l:
        s.add(genus(*t))
    return s


def index(D):
    c = Cl(D)
    g = genera(D)
    assert len(c) % len(g) == 0
    return len(c) // len(g)
