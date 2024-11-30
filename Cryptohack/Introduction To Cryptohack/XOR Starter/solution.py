def xor(str, num):
    encrypted_msg = ''

    for i in range(0, len(str)):
        encrypted_msg += chr(ord(str[i]) ^ num)

    return encrypted_msg


str = 'label'
num = 13

print(xor(str, num))
