from util import p
from sympy import Matrix, pprint


def dot_product(matrix, vector):
    result = []
    for i in range(len(vector)):
        suma = 0
        for j in range(len(vector)):
            suma += matrix[i][j] * vector[j]
        result.append(suma % p)
    return result


def decode(vandermonde, received):
    #print(vandermonde)
    A = Matrix(vandermonde)
    vand_inv = A.inv_mod(p)
   # print("Vand inv: \n")
   # print(vand_inv)
    free_vect = Matrix(received)
    res = vand_inv * free_vect
    final_res = []
    for i in res:
        final_res.append(i % p)
    return final_res


def convert_to_binary(int_vector):
    trim_free_coef = int_vector[1:]
    result = []
    for i in trim_free_coef:
        result.append(int(i).to_bytes(32, byteorder='big'))
    return result


def retrieve_message(int_vector):
    byte_array = convert_to_binary(int_vector)
    result = ""
    for i in byte_array:
        result += i.decode()
    return result

