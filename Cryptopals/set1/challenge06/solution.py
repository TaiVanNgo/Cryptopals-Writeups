from itertools import combinations


def bytes_xor(a, b) -> bytes:
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


def hamming_distance(a: bytes, b: bytes) -> int:
    return sum(weights[byte] for byte in bytes_xor(a, b))


def _get_hamming_weights() -> dict[int, int]:
    weights: dict[int, int] = {0: 0}
    pow_2 = 1

    for _ in range(8):
        for k, v in weights.copy().items():
            weights[k+pow_2] = v+1
        pow_2 <<= 1
    return weights


weights = _get_hamming_weights()

MAX_KEYSIZE = 40


def guess_keysize(ct: bytes, num_guesses: int = 1) -> list[tuple[float, int]]:
    def get_score(size: int) -> float:
        chunks = (ct[:size],
                  ct[size:2*size],
                  ct[2*size:3*size],
                  ct[3*size:4*size],
                  )
        avg = sum(hamming_distance(a, b)
                  for a, b in combinations(chunks, 2)) / 6
        return avg / size

    scores = [(get_score(size), size) for size in range(2, MAX_KEYSIZE)]
    scores.sort()

    return scores[:num_guesses]


def crack_repeating_key_xor(ciphertext: bytes, keysize: int) -> tuple[float, bytes]:
    chunks = [ciphertext[i::keysize] for i in range(keysize)]
    cracks = 


if __name__ == '__main__':
    assert hamming_distance(b'this is a test', b'wokka wokka!!!') == 37
