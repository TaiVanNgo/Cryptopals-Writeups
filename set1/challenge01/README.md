# Convert hex to base64
Author: Van Tai

## Description
The string: `49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d`

Should produce:
`SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t`

So go ahead and make that happen. You'll need to use this code for the rest of the exercises. Cryptopals Rule

RULE
>Always operate on raw bytes, never on encoded strings. Only use hex and base64 for pretty-printing.


## Writeups
The challenges want me to convert a hex into a base64 type. Initially, it gives the hex numbers under the `string` type. 

base64 is the way of encoding, one character in base64 will have 6bits. -> [more info](https://en.wikipedia.org/wiki/Base64)

STRATEGY: First, convert hex to the raw bytes first, then convert the bytes to the base64. That's how the base64 works.

In the code, import the library `base64` to encode the base64 easily.

use `bytes()` to convert the original value to hex value, but our value is `hex` -> we use bytes.fromhex([input string]) -> we got the raw bytes.

After we get the bytes, we can convert it into base64 by using `base64.b64encode([input])`
BUTTTT, if we only use the `b64encode` it will return the value BUT in the raw bytes, we need to convert to the ascii text, by using `decode()`

Then, it will be `base64.64encode([input]).decode()`




