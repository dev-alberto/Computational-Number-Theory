from random import randint


def jacobi(a, n):
    """
    Return Jacobi symbol (or Legendre symbol if n is prime)
    """
    s = 1
    while True:
        if n < 1:
            raise ValueError("Too small module for Jacobi symbol: " + str(n))
        if n % 2 == 0:
            raise ValueError("Jacobi is defined only for odd modules")
        if n == 1:
            return s
        a = a % n
        if a == 0:
            return 0
        if a == 1:
            return s

        if a % 2 == 0:
            if n % 8 in (3, 5):
                s = -s
            a //= 2
            continue

        if a % 4 == 3 and n % 4 == 3:
            s = -s

        a, n = n, a


def strassen(n, k):
    while k > 0:
        a = randint(2, n-2)
        x = jacobi(a, n)
        if x == 0 or pow(a, (n-1) // 2, n) != (x % n):
            return "compus"
        k -= 1
    return "posibil prim"

print(strassen(113, 7))
