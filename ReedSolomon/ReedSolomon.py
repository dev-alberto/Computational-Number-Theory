from arrived import noisy_received_message, noisy_simple_received_message
from Lagrange import make_vandermonde_matrix
from decoding import decode, retrieve_message

vandermonde, trimmed_received = make_vandermonde_matrix(noisy_simple_received_message)
original_poly = decode(vandermonde, trimmed_received)
original_message = retrieve_message(original_poly)

f = open("simpleM", "r")
text = f.read()

if original_message == text:
    print("ok")