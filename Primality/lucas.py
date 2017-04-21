from time import time


def lucas(p):
    s = 4
    M = 2**p - 1
    for i in range(p-2):
        s = (s * s - 2) % M
    return s == 0


def fast_lucas(p):
    s = 4
    M = 2**p - 1
    for i in range(p-2):
        square = s * s
        s = (square & M) + (square >> p)
        if s >= M:
            s -= M
        s -= 2
    return s == 0

if __name__ == '__main__':
    # start = time()
    # print(lucas(9689))
    # print(time() - start)

    start1 = time()
    print(fast_lucas(86243))
    print(time() - start1)