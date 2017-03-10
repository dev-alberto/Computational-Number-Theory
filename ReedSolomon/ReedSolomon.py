from arrived import simple_encoding
from Lagrange import make_vandermonde_matrix
from util import p
from decoding import decode, retrieve_message

#print(simple_encoding)
#print("***********")
vandermonde, trimmed_received = make_vandermonde_matrix(simple_encoding)
#print("****")
#print(trimmed_received)
#print("*******")
original_poly = decode(vandermonde, trimmed_received)
#print(original_poly)
original_message = retrieve_message(original_poly)

print(original_message)

f = open("simpleM", "r")


