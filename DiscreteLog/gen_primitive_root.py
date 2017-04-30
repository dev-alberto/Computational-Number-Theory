from util import getPrime, isProbablePrime, jacobi_symbol, inv
from random import randint
from math import ceil, sqrt

#Generate α, a primitive root modulo a prime p, where p is an odd prime, using
#one of the algorithms discussed in class (assume that the prime factorization
#of p − 1 is known in advance - the simplest choice will be p = 2q + 1, where
#p and q are odd primes).
def get_special_prime(bits):
    flag = True
    while flag:
        q = getPrime(bits)
        p = 2 * q + 1
        if isProbablePrime(p):
            flag = False
            return p


def genPrimeRoot(bits):
    p = get_special_prime(bits)
    alpha = randint(2, p-2)
    if jacobi_symbol(alpha, p) == 1:
        alpha = p - alpha
    return alpha, p


#For p and α generated as above and an arbitrary β ∈ Zp*, compute the discrete
#logarithm logα β modulo p, using one of the algorithms discussed in class
#(Skanks or Pollard). Use moderate-sized primes (e.g., p is on 32 bits). (4p)

def shanks(bits):
    alpha, p = genPrimeRoot(bits)
    print("p is: " + str(p))
    print("alpha is: " + str(alpha))
    beta = randint(1, p-1)
    print("beta is: " + str(beta))
    m = ceil(sqrt(p-1))
    L = {}
    for i in range(m):
        L[i] = pow(alpha, i, p)
    alpha_inv_m = inv(pow(alpha, m), p)
    y = beta
    for i in range(m):
        for k in L:
            if y == L[k]:
                return i * m + k
        y = y * alpha_inv_m % p

print(shanks(16))
