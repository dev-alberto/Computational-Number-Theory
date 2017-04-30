from time import time


def lucas_slow(p):
    s = 4
    mp = 2 ** p -1
    for i in range(p-2):
        s = (s**2 - 2) % mp
    return s == 0


def modf(n, p, mp):
    while n > mp:
        #cei mai nesimnificativi p biti a lui n + bitii ramasi sunt echivalenti cu m % mp. Repetam pana cel mult p biti raman
        n = (n & mp) + (n >> p)
    if n == mp:
        return 0
    else:
        return n


def lucas(p):
    s = 4
    mp = 2 ** p - 1
    for i in range(p - 2):
        s = modf(s**2 - 2, p, mp)
    return s == 0


if __name__ == '__main__':
    start = time()
    print(lucas(23209))
    print(time() - start)

    start1 = time()
    print(lucas_slow(23209))
    print(time() - start1)
