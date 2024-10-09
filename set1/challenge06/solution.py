from os import urandom


def hw_1(byte):
    return bin(byte).count("1")


def hw_2(byte):
    weight = 0
    while byte != 0:
        weight += byte & 1
        byte >>= 1

    return weight


def hw_3(byte):
    byte = (byte & 0x55) + ((byte >> 1) & 0x55)
    byte = (byte & 0x33) + ((byte >> 1) & 0x33)
    byte = (byte & 0x0F) + ((byte >> 1) & 0x0F)
    return byte


def hw_4(byte):
    weight = 0
    while byte > 0:
        byte &= byte - 1
        weight += 1
    return weight


def bxor(a, b):
    cipher_text = bytearray()  # define a bytearray
    for i in range(len(a)):
        cipher_text.append(a[i] ^ b[i])  # append to the array

    # convert to byte again
    return bytes(cipher_text)


def hd(a, b, hw):
    distance = 0
    for byte in bxor(a, b):
        distance += hw(byte)

    return distance


a, b = urandom(100), urandom(100)
 
print(hd(a, b, hw_1))
