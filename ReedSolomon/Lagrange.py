from util import p, inv
import itertools


def partial_interpolation(A, received):
    """Returns free coefficient"""
   # return sum(enc[i] * j * inv((j-i), p) for i, j in A if i != j)
    s = 0
    for i in A:
        for j in A:
            if i != j:
                s += received[i] * j * inv(j-i, p)
    return s % p


def get_combinations(received):
    a = [i for i in range(len(received))]
    return list(itertools.combinations(a, len(a) - 2))

#print(z)
#print(partial_interpolation([0, 2], z))


def make_A():
    pass


def trim_received_poly(A, received):
    for i in range(len(received)):
        if i not in A:
            del received[i]
    return received


def make_vandermonde_matrix(received):
    """Returns Vandermonde matrix used for finding out Lagrange poly coefficients and the trimmed received vector """
    result = [[0 for x in range(3)] for x in range(3)]

    A = make_A()
    received = trim_received_poly(A, received)

    for i in received:
        for j in A:
            result[i][j] = (i ** j) % p
    return result, received

