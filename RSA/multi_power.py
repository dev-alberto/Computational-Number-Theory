from util import getPrime, inv, gcd
from random import randrange
from time import time
from datetime import timedelta


def gen_keys():
    p = getPrime(512)
    q = getPrime(512)
    p_s = p ** 2
    n = p_s * q
    phi = (p_s - p) * (q - 1)
    e = randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = randrange(1, phi)
        g = gcd(e, phi)
    e = 41
    d = inv(e, phi)

    dp = d % (p - 1)
    dq = d % (q - 1)

    p2_inv_q = inv(p_s, q)
    e_inv_p = inv(e, p)
    #public, private
    return [(n, e), (p, q, dp, dq, p2_inv_q, e_inv_p), d]


def encrypt(public, m):
    return pow(m, public[1], public[0])


def hensel(cp, dp, p, e_inv_p, e, c):

    p_s = p**2
    m_p = pow(cp, dp-1, p)
    K0 = m_p * cp % p
    A = -pow(K0, e, p_s)
    A = (A + c) % p_s
    m_p = m_p * A % p_s
    m_p = m_p * e_inv_p % p_s
    m_p = (m_p + K0) % p_s

    return m_p


def decrypt(c, privk, pub):

    p, q, dp, dq, p2_inv_q, e_inv_p = privk
    n, e = pub

    p_s = p**2
    c_p = c % p_s
    c_q = c % q
    m_p = hensel(c_p, dp, p, e_inv_p, e, c)
    m_q = pow(c_q, dq, q)
    V = (m_q - m_p) % q
    V = V * p2_inv_q % q
    M = V * p_s % n
    M = (M + m_p) % n

    return M


def classic_decrypt(c, d, n):
    return pow(c, d, n)

if __name__ == '__main__':
    m_ = 65
    public, private, d = gen_keys()
    #print(public)
    c = encrypt(public, m_)

    start_hensel = time()
    dec = decrypt(c, private, public)
    elapsed = time() - start_hensel
    print(str(timedelta(seconds=elapsed)))

    delta1 = timedelta(seconds=elapsed)

    print(dec)

    start_normal = time()
    dec_ = classic_decrypt(c, d, public[0])
    elapsed_ = time() - start_normal
    print(str(timedelta(seconds=elapsed_)))
    delta2 = timedelta(seconds=elapsed_)

    print(dec_)

    print(delta2/delta1)