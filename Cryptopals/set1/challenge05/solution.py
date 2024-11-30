def bxor(message: bytes, key: bytes) -> bytes:
    # define byte array
    cipher_text: bytearray = bytearray()

    for i in range(len(message)):
        cipher_text.append(message[i] ^ key[i % len(key)])

    # Convert to bytes again and return
    return bytes(cipher_text)


plain_text = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
plain_text_bytes = bytes(plain_text, 'utf-8')

key = "ICE"
key_bytes = bytes(key, 'utf-8')

encrypted_text_bytes = bxor(plain_text_bytes, key_bytes)
encrypted_hex_string = encrypted_text_bytes.hex()
print(encrypted_hex_string)
