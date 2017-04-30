from random import getrandbits, randrange
from itertools import repeat


### Fast prime test ###
def isProbablePrime(n, t=7):
    """Miller-Rabin primality test"""

    def isComposite(a):
        """Check if n is composite"""
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2 ** i * d, n) == n - 1:
                return False
        return True

    assert n > 0
    if n < 3:
        return [False, False, True][n]
    elif not n & 1:
        return False
    else:
        s, d = 0, n - 1
        while not d & 1:
            s += 1
            d >>= 1
    for _ in repeat(None, t):
        if isComposite(randrange(2, n)):
            return False
    return True


### Generate random prime ###
def getPrime(n):
    """Get a n-bit prime"""

    p = getrandbits(n)
    while not isProbablePrime(p):
        p = getrandbits(n)
    return p


def jacobi_symbol(a, b):
    if (b < 0) or (b % 2 == 0):
        return 0
    j = 1
    if a < 0:
        a = -a
        if b % 4 == 3:
            j = -j
    while a != 0:
        while a % 2 == 0:
            #procesam multiplii de 2
            a //= 2
            if (b % 8 == 3) or (b % 8 == 5):
                j = -j

        # Legea reciprocitatii
        a, b = b, a
        if a % 4 == 3 and b % 4 == 3:
            j = -j
        a = a % b
    if b == 1:
        return j
    else:
        return 0


####### Euclid #######
def gcd_extended(a, b):
    """ax + by = gcd(a, b)
    :return (x, y, gcd(a,b))"""
    s, old_s, t, old_t, r, old_r = 0, 1, 1, 0, b, a
    while r:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_s, old_t, old_r


####### Invers Modular #######
def inv(a, n):
    """Find the modular inverse x, ax = 1 mod n"""

    i = gcd_extended(a, n)[0]
    while i < 0:
        i += n
    return i