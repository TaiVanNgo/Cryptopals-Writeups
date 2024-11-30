# readable text list from a-z (including the space " ")
readable_text_list = list(range(97, 122)) + [32]


def bxor(message: bytes, key: bytes) -> bytes:
    cipher_text: bytearray = bytearray()  # define a bytearray

    # Loop over the length of message (assuming message and key are the same length)
    for i in range(len(message)):
        cipher_text.append(message[i] ^ key[i])

    # Convert to bytes again and return
    return bytes(cipher_text)


def attack_single_byte_xor(cipher_text: bytes) -> dict:
    best: dict = None

    for i in range(2**8):
        candidate_key: bytes = i.to_bytes(1, byteorder='big')

        # duplicate the length of candidate key to the length of cipher text
        key_stream = candidate_key * len(cipher_text)
        candidate_message = bxor(cipher_text, key_stream)

        number_of_letters = sum(
            [x in readable_text_list for x in candidate_message])

        if best == None or number_of_letters > best['number_of_valid_letters']:
            best = {
                "message": candidate_message,
                "key": candidate_key,
                "number_of_valid_letters": number_of_letters
            }

    return best


def find_encrypted_string(line_list) -> dict:
    best_result: dict = None  # store the best result

    for hex_string in line_list:
        hex_bytes = bytes.fromhex(hex_string)  # conver the hex to bytes
        result: dict = attack_single_byte_xor(hex_bytes)

        if best_result == None or result['number_of_valid_letters'] > best_result['number_of_valid_letters']:
            best_result = result

    return best_result


with open('text.txt', 'r') as text_file:
    line_list = [line.strip() for line in text_file.readlines()
                 ]  # Strips the '\n' from each line

result: dict = find_encrypted_string(line_list)

print(result)
