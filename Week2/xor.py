#! /bin/python
__author__ = "glender"
__copyright__ = "Copyright (c) 2018 glender"
__credits__ = [ "glender" ]
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "glender"
__email__ = "None"
__status__ = "Production"

import string
import collections
import sets

# XORs two string
def strxor(a, b):     # xor two strings (trims the longer input)
    return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b)])

# string to hex
def toHex(x):
    return "".join([hex(ord(c))[2:].zfill(2) for c in x])

firstMessage = "Hi There"
secondMessage = "The ones"
key = "THEKEYZz"

# ciphertext (in hex format)
c1 = toHex(strxor(firstMessage, key))
ciphers = [c1]
# The target ciphertext we want to crack
target_cipher = toHex(strxor(secondMessage, key))

# the target and ciphertext xor'ed together
xoredTogether = toHex(strxor(c1.decode('hex'), target_cipher.decode('hex')))

# display the results for c1, target cipher, and the two xor'ed together
print c1
print target_cipher
print xoredTogether
print

# the alphabet, including space
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz "

attackLetters = []
locationOfLetters = []
possibleKeys = []

for letter in alpha:
    # is the character within our cipher?
    if toHex(letter) in c1: 
        # is the hex value in the correct spot? meaning at an even index
        if c1.index(toHex(letter)) % 2 == 0:
            attackLetters.append(toHex(letter))
            locationOfLetters.append(c1.index(toHex(letter)) / 2)
            
    # is the character within our cipher?
    if toHex(letter) in target_cipher:   
        # is the hex value in the correct spot? meaning at an even index
        if target_cipher.index(toHex(letter)) % 2 == 0:
            attackLetters.append(toHex(letter))
            locationOfLetters.append(target_cipher.index(toHex(letter)) / 2)

# determine the possible key
count = 0
for HEX in attackLetters:
    possible = []
    for letter in alpha:
        val = strxor(letter, HEX.decode('hex'))
        # is the value within the character set? 
        if val in alpha:
            possible.append(val)

    print HEX
    print possible
    print "At location: " + str(locationOfLetters[count])
    print 
    count +=1
