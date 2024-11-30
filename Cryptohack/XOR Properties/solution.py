# KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
# KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
# KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
# FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf

def xor(key1, key2):
    return bytes(b1 ^ b2 for b1, b2 in zip(key1, key2))


KEY1 = 'a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'
key1_bytes = bytes.fromhex(KEY1)

tmp = '37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e'
tmp_bytes = bytes.fromhex(tmp)
key2_bytes = xor(key1_bytes, tmp_bytes)

tmp = 'c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'
tmp_bytes = bytes.fromhex(tmp)
key3_bytes = xor(key2_bytes, tmp_bytes)

tmp = '04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'
tmp_bytes = bytes.fromhex(tmp)

key13_bytes = xor(key1_bytes, key3_bytes)
key132_bytes = xor(key13_bytes, key2_bytes)

tmp = '04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'
tmp_bytes = bytes.fromhex(tmp)

flag = xor(key132_bytes, tmp_bytes)
print(flag)
