from random import randint


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


def strassen(n, k):
    while k > 0:
        a = randint(2, n-2)
        x = jacobi_symbol(a, n)
        if x == 0 or pow(a, (n-1) // 2, n) != (x % n):
            return "compus"
        k -= 1
    return "posibil prim"

print(strassen(997, 7))
