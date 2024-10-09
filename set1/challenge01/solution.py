import base64

hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
print ("original hex string: ", hex_string)

hex_bytes = bytes.fromhex(hex_string)
print("hex string after converted to bytes presentation: ", hex_bytes)

# convert the bytes to base64
base64encoding = base64.b64encode(hex_bytes).decode();
print("base64 encode: ", base64encoding)
