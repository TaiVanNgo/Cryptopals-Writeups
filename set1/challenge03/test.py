def bxor(message, key):
    cipher_text = bytearray() # define a bytearray
    for i in range(len(message)):
        cipher_text.append(message[i] ^ key[i]) # append to the array

    # convert to byte again and print
    return bytes(cipher_text)

#TEST 
#origin hex string
hex_string = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
# convert to bytes
hex_bytes = bytes.fromhex(hex_string)

possible_key = bytes([1])

key_stream = possible_key * len(hex_bytes) #Repeat the key so it has the same length with the message

encryptedMessage = bxor(hex_bytes, key_stream)

print(encryptedMessage)


#TEST

def letterRatio(input_bytes):  
    #returning the number of ascii value appears in the input_bytes
    nb_letters = sum([ x in ascii_text_list for x in input_bytes])

    return nb_letters / len(input_bytes)

def isProbablyText(input_bytes):
    ratio = letterRatio(input_bytes)

    return ratio > 0.7 # it retruns true if ratio > 0.7 and vice versa

ascii_text_list = list(range(97, 122)) + [32] #An array of ascii value from a-z (including the space " ")
print(sum([ x in ascii_text_list for x in b'hi! World?']))
