from util import inv
from time import time


def decriptareClasica(c, n, d):
    return pow(c, d, n)


def hensel(c, p2, p, d):
    return pow(c % p2, d % (p-1), p)


def decriptareEficienta(c, d, p, q, n, p2, p2_inv_q):

    xp = hensel(c, p2, p, d)
    xq = pow(c % q, d % (q-1), q)

    # Aplicare Garner
    V = (xq - xp) % q
    V = V * p2_inv_q % q
    M = V * p2 % n
    M = (M + xp) % n
    return M


if __name__ == '__main__':

    _p = 4231596253430823389450295914636238845992269369171494862563985556193763024777786413956717992176625075346621562657254102981765704095082912361295948082031523
    _q = 12820849163256526849325478940172390410571957465007039047342221033050785981274945947107604533587227851215125266830612044781035431668179954251982524625736101
    _p_2 = _p**2
    e = 41
    mesaj = 234

    _n = _p_2 * _q
    phi = (_p_2 - _p) * (_q - 1)
    _d = inv(e, phi)
    _p2_inv_q = inv(_p_2, _q)

    criptotext = pow(mesaj, e, _n)

    start1 = time()

    print(decriptareClasica(criptotext, _n, _d))

    end1 = time() - start1

    start2 = time()

    print(decriptareEficienta(criptotext, _d, _p, _q, _n, _p_2, _p2_inv_q))

    end2 = time() - start2

    print(end1 / end2)
