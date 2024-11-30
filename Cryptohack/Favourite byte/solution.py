def crack_xor(cipher):
    for potential_key in range(0, 256):  # run from 0 to 256
        # try to decrypt wiht potential key
        decrypted_msg = bytes(c ^ potential_key for c in cipher)

        if (decrypted_msg.startswith(b'crypto')):
            return decrypted_msg.decode('utf-8', errors='ignore')

    return None


cipher = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'
cipher_bytes = bytes.fromhex(cipher)

print(crack_xor(cipher_bytes))
