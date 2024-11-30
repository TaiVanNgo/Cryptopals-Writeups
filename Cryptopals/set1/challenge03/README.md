# Single-byte XOR cipher
Author: Tai Ngo

## Description
The hex encoded string:

    1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736

... has been XOR'd against a single character. Find the key, decrypt the message.

You can do this by hand. But don't: write code to do it for you.

How? Devise some method for "scoring" a piece of English plaintext. Character frequency is a good metric. Evaluate each output and choose the one with the best score.

> Achievement Unlocked
>
>You now have our permission to make "ETAOIN SHRDLU" jokes on Twitter.

## Writeups

Firsly, I defined a bxor message to help me convert the message with the key (go to the set 1 challenge 2 to see the details)

### The ascii_text_list explanation
the ascii_text_list is the list (or an array) contains the ascii value from 97 to 122. Which means it consists the corresponding characters from a to z (a-z), I also append the ascii value at 32, which is an empty space (" ")


### Introduction to the main funciton
Our approach is brute force to see the best key for this cipher.

First of all, I declare a variable `best`, which is a [dictionary in Python](https://www.w3schools.com/python/python_dictionaries.asp). It will contains {message, key, number of valid letters}, I will describe these attributes later


We will loop through the number of 0 to 256, WHY?, yes because this is a problem of single-byte right? 1 byte has 8-bits, or you can use this formular (2^n - 1), n is the number of bits. Then we have 2^8 - 1 = 255. Thus, if we have 8 bits it can represent number from 0 to 255. You can try by calculating it by hand.

=> The `i` will run from 0 -> 255 as we want to try every possible byte.

### Explaination of each variable in the functoin
1. `candidate_key`: it will be a byte of every numbers.Using `[number].to_bytes(1, byteorder='big')`, number 1 means that we use 1 byte, the `byteorder='big'` because it is big, don't ask me why, I dont know :>
2. `key_stream = candidate_key * len(cipher_text)`, using this to duplicate the single key to have the same length with the cipher text.

For example, if we have a key of `b'\x01'` if we multiply it with 5. The result is `b'\x01\x01\x01\x01\x01'` -> since our `bxor` function need the message and the key have the same length.

3. `candidate_message`: is the possible message that we recieve from the `bxor` function, providing them with cipher message and the candidate keystream.

4. `number_of_letters`: this will store the number of valid characters in the reusult (the `candidate_message`).

Let I break it into smaller piecies:
In Python, it can regconize the given byte is equal the ascii character or not. In our `ascii_text_chars` we define it has the value from `[a-z]`, include the empty space as well `" "`.
So, for this code, x will go to each character of the bytes we give to it, for example `b'hi! World?`
we use
`[ x in ascii_text_chars for x in b'hi! World?']`
x will be `b'h'` then `b'i'`, the Python will check if the x is in the ascii list or not. It return true and false
the result for this example will be

`[True, True, False, True, False, True, True, True, True, False]`

You understand why right?, the `False` is for the `!` and `?` characters, and also the capital letter `W` as we define the list only contains from a-z

we comprise it with the [sum](https://www.geeksforgeeks.org/python-count-true-booleans-in-a-list/) to get the number of the True value

`sum([ x in ascii_text_chars for x in b'hi! World?'])`

--> `sum([True, True, False, True, False, True, True, True, True, False])`

--> sum = 7 (7 true)


### Final Check

The final check will consider if the current key and decrypted message is the best or not. 

It checks by the `number_of_letters` is larger than the current number of valid letters stored in the `best` or not. Except for the first iteration when the best still None, we will store it.

### Using function and result

Finally, we can reach this step, I simply copy the hexa string and convert it to the bytes. After that I put it into the function and wait for the result

**RESULT**:
Decrypted Message: b"Cooking MC's like a pound of bacon"

The Correct Key to decrypt this message: b'X'

The number of valid characters: 30
 