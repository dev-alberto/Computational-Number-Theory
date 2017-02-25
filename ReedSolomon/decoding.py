from numpy.linalg import inv
from util import p


def dot_product(matrix, vector):
    result = []
    for i in range(len(vector)):
        suma = 0
        for j in range(len(vector)):
            suma += matrix[i][j] * vector[j]
        result.append(suma % p)
    return result


def decode(vandermonde, received):
    inv_vandermonde = inv(vandermonde)
    return dot_product(inv_vandermonde, received)


def convert_to_binary(int_vector):
    result = []
    for i in int_vector:
        result.append(i.to_bytes(32, byteorder='big'))
    return result


def retrieve_message(int_vector):
    byte_array = convert_to_binary(int_vector)
    result = ""
    for i in byte_array:
        result += i.decode()
    return result

