from arrived import simple_encoding, noisy_simple_received_message, complex_encoding, noisy_complex_received
from Lagrange import make_vandermonde_matrix
from decoding import decode, retrieve_message

#print(simple_encoding)
#print("***********")
vandermonde, trimmed_received = make_vandermonde_matrix(noisy_complex_received)
#print("****")
#print(trimmed_received)
#print("*******")
original_poly = decode(vandermonde, trimmed_received)
#print(original_poly)
original_message = retrieve_message(original_poly)

print(original_message)


