from util import p, inv
import itertools
from numpy import prod


# def partial_interpolation(A, received):
#     """Returns free coefficient"""
#    # return sum(enc[i] * j * inv((j-i), p) for i, j in A if i != j)
#     s = 0
#     for i in A:
#         numarator = 1
#         numitor = 1
#         for j in A:
#             if j != i:
#                 #product *= j * inv(j-i, p)
#                 numarator *= j
#                 numitor *= j-i
#         product = numarator * inv(numitor, p)
#         s += received[i-1] * product
#     return s % p


def efficient_partial_interpolation(A, received):
    numitor = []
    for i in A:
        for j in A:
            numitor.append(j-i)
    elimina_duplicate = set(numitor)
    elimina_duplicate.discard(0)
    _numitor = list(elimina_duplicate)
    numarator = []
    for i in A:
        l = [j for j in A if j != i]
        num = [j-i for j in A if j != i]
        _l = [k for k in _numitor if k not in num]
        coeff = l + _l
        numarator.append((received[i-1] * prod(coeff)) % p)
    return (sum(numarator) * inv(prod(_numitor), p)) % p


def get_combinations(received):
    a = [i+1 for i in range(len(received))]
    return list(itertools.combinations(a, len(a) - 2))

#print(z)
#print(partial_interpolation([0, 2], z))


def make_A(received):
    A_canditates = get_combinations(received)
    for i in A_canditates:
        #if partial_interpolation(i, received) == 1:
        if efficient_partial_interpolation(i, received) == 1:
            return i


def trim_received_poly(A, received):
    new_A = [i-1 for i in A]
    result = [received[i] for i in new_A]
    return result


def make_vandermonde_matrix(received):
    """Returns Vandermonde matrix used for finding out Lagrange poly coefficients and the trimmed received vector """

    A = make_A(received)
    print(A)
    received = trim_received_poly(A, received)
    result = [[0 for x in range(len(received))] for x in range(len(received))]

    _A = [i for i in range(len(A))]

    # for i in A:
    #     for j in A:
    #         result[i-1][j-1] = pow(i, j-1, p)
    for i in _A:
        for j in _A:
            result[i][j] = pow(A[i], j, p)

    return result, received
