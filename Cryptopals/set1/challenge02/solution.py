from binascii import hexlify

hex_string1 = '1c0111001f010100061a024b53535009181c'
hex_string2 = '686974207468652062756c6c277320657965'

# Convert these hex string to raw bytes
bytes_1 = bytes.fromhex(hex_string1)
bytes_2 = bytes.fromhex(hex_string2)
print(f"The hex string number 1 in raw bytes: {bytes_1}")
print(f"The hex string number 2 in raw bytes: {bytes_2}\n")

bytes_list = []

for i in range(len(bytes_1)):
    # perform XOR operation on each byte
    bytes_list.append(bytes_1[i] ^ bytes_2[i])
    # the XOR operation return a ascii value (0 - 255)
# the bytes_list after the for loop will be an array of decimal, the decimal here is
# the ascii value in the value after them xor with each other
print(f"The list of ascii value after XOR: {bytes_list}")

# convert it to raw bytes
bytes_result = bytes(bytes_list)
print("The result in raw bytes: ", bytes_result)

# Convert it back to hexadecimal
print("The final result: ", hexlify(bytes_result).decode())
