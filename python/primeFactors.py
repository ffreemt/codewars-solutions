"""
https://www.codewars.com/kata/54d512e62a5e54c96200019e/train/python

test.assert_equals(primeFactors(7775460), "(2**2)(3**3)(5)(7)(11**2)(17)")
"""

_ = """
import subprocess as sp
import shlex

try:
    from sympy import primefactors
except ModuleNotFoundError:
    command = shlex.split("pip install sympy --user")
    proc = sp.Popen(command, stdout=-1, stderr=-1)
    print(" ".join(command) + "...")
    out, err = proc.communicate()
    if err:
        sys.stderr.write('\n\t >>>> error: %s' % err.decode())
    sys.stdout.write('\n\t>>> %s' % out.decode())
    from sympy import primefactors
# """

def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac

def primeFactors(n):
    """ primeFactors.

    >>> primeFactors(1)
    '(1)'
    >>> primeFactors(7775460)
    '(2**2)(3**3)(5)(7)(11**2)(17)'
    """
    if n == 1:
        return f"({n})"

    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)

    res = ""
    for elm in sorted(list(set(primfac))):
        count = primfac.count(elm)
        if count == 1:
            res += f"({elm})"
        else:
            res += f"({elm}**{count})"

    return res


def test_sanity():
    """ test sanity. """
    assert primeFactors(1) == "(1)"


def test1():
    """ test1. """
    assert primeFactors(7775460) == "(2**2)(3**3)(5)(7)(11**2)(17)"
