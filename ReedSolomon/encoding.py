from util import p


def read_binary(msg, buffer=32):
    """Reads a message and returns an array of bytes, each element containing 32 bytes, or 256 bits"""
    f = open(msg, 'rb')
    result = []
    bloc = f.read(buffer)
    while bloc:
        result.append(bloc)
        bloc = f.read(buffer)
    return result


def convert_to_int(byte_arr):
    """Converts an array of bytes into an array of integers"""
    result = []
    for i in byte_arr:
        result.append(int.from_bytes(i, byteorder='big'))

    #introducem termenul liber
    result.insert(0, 1)

   # print(result)
    return result


def poly_horner_eval(poly, i):
    """Evaluates given polynomial poly in given i point"""
    val = 0
    for coeff in reversed(poly):
        val = val*i + coeff
    return val % p


def create_encoding(filename):
    binary_bloc = read_binary(filename)
    int_bloc = convert_to_int(binary_bloc)
    #print("INT BLOC: ")
    #print(int_bloc)
    encoding = []
    for i in range(1, len(int_bloc) + 3):
        #y1, y2, ..., yn
        #poly_horner_eval(int_bloc, i)
        encoding.append(poly_horner_eval(int_bloc, i))
    #print(encoding)
    return encoding


#print(poly_horner_eval([1, 0, 2], 2))
#print(create_encoding("simpleM"))
