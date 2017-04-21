from util import getPrime, inv, gcd
from random import randrange
from time import time
from datetime import timedelta

# def gen_message(filename):
#     f = open(filename, 'rb')
#     info = f.read(100)
#     return int.from_bytes(info, byteorder='big')


def gen_multi_prime_keys():
    p = getPrime(512)
    q = getPrime(512)
    r = getPrime(512)
    #print("primes are :" + str(p) + " " + str(q) + " " + str(r))
    print(p, q, r)
    n = p * q * r
    phi = (p-1) * (q-1) * (r-1)
    e = randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = randrange(1, phi)
        g = gcd(e, phi)
    e = 41
    d = inv(e, phi)
    #print("d is: " + str(d))
    return [(n, e), (n, d), (p, q, r)]


def encrypt(m, public_k):
    return pow(m, public_k[1], public_k[0])


def classic_decrypt(c, priv_k):
    return pow(c, priv_k[1], priv_k[0])


# def CRT(b, m):
#     _x = 0
#     #_m = prod(m)
#     _m = 1
#     for i in m:
#         _m *= i
#     print("prod is " + str(_m))
#     M = [0 for i in range(len(m))]
#     y = [0 for i in range(len(m))]
#     for i in range(len(m)):
#         print("***")
#         #print(_m / m[i])
#         M[i] = int(_m / m[i])
#         print("M[i] is " + str(M[i]))
#         y[i] = inv(M[i], m[i])
#         print("y[i] is " + str(y[i]))
#         G = (y[i] * M[i]) % _m
#
#         G = (G * b[i]) % _m
#
#         _x = (_x + G) % _m
#
#     print("***")
#     print("res is: " + str(_x))
#     return _x


def Garner(primes, x_p, x_q, x_r, n):
    p_inv = inv(primes[0], primes[1])
    pq_inv = inv(primes[0] * primes[1], primes[2])
    V = (x_q - x_q) % primes[1]
    V = V * p_inv % primes[1]
    x_pq = V * primes[0] % (primes[0] * primes[1])
    x_pq = (x_pq + x_p) % (primes[0] * primes[1])
    V = (x_r - x_pq) % primes[2]
    V = V * pq_inv % primes[2]
    M = V * primes[0] % n
    M = M * primes[1] % n
    M = (x_pq + M) % n
    return M


# def decrypt_using_crt(c, d, primes):
#    # print("d is " + str(d))
#     #print("primes are :" + str(primes[0]) + " " + str(primes[1]) + " " + str(primes[2]))
#
#     x_p = pow(c % primes[0], d % (primes[0]-1), primes[0])
#     x_q = pow(c % primes[1], d % (primes[1]-1), primes[1])
#     x_r = pow(c % primes[2], d % (primes[2]-1), primes[2])
#     print(x_q, x_q, x_r)
#     return CRT([x_p, x_q, x_r], primes)


def decrypt_using_garner(c, d, primes, n):
    x_p = pow(c % primes[0], d % (primes[0] - 1), primes[0])
    x_q = pow(c % primes[1], d % (primes[1] - 1), primes[1])
    x_r = pow(c % primes[2], d % (primes[2] - 1), primes[2])
    return Garner(primes, x_p, x_q, x_r, n)


if __name__ == '__main__':
    m_ = 65
    public, private, _primes = gen_multi_prime_keys()
    _c = encrypt(m_, public)

    start_garner = time()
    dec = decrypt_using_garner(_c, private[1], _primes, public[0])
    elapsed = time() - start_garner
    print(str(timedelta(seconds=elapsed)))
    delta1 = timedelta(seconds=elapsed)

    start_normal = time()
    dec_ = classic_decrypt(_c, private)
    elapsed_ = time() - start_normal
    print(str(timedelta(seconds=elapsed_)))

    delta2 = timedelta(seconds=elapsed_)

    print(dec)
    print(dec_)

    print(delta2/delta1)
