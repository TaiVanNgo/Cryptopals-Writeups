def bxor(message, key):
    cipher_text = bytearray()  # define a bytearray
    for i in range(len(message)):
        cipher_text.append(message[i] ^ key[i])  # append to the array

    # convert to byte again
    return bytes(cipher_text)


# -----------------------------------------------------------------------------
# An array of ascii value from a-z (including the space " ")
ascii_text_list = list(range(97, 122)) + [32]


def attack_single_byte_xor(cipher_text):
    # A dictionary to keep track the best candidate
    best = None

    # since we do with a byte -> a byte consists of 8 bits, so we find all the possible key from
    # 0 -> 255
    for i in range(2**8):
        # convert the candidate key from a number to byte
        candidate_key = i.to_bytes(1, byteorder='big')  # from (0x00 to 0xff)
        # make a candidate_key have the same length with the encrypted text
        key_stream = candidate_key * len(cipher_text)
        candidate_message = bxor(cipher_text, key_stream)
        number_of_letters = sum(
            [x in ascii_text_list for x in candidate_message])

        # if the candidate key (possible key) has more valid letter than the other candidate before
        # we store it to best
        if best == None or number_of_letters > best['number_of_valid_letters']:
            # store the best key
            best = {
                "message": candidate_message,
                'key': candidate_key,
                "number_of_valid_letters": number_of_letters
            }

    return best


hex_string = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
hex_bytes = bytes.fromhex(hex_string)

result = attack_single_byte_xor(hex_bytes)

print(result)
