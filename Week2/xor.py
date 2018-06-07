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

def toHex(x):
    toHex = "".join([hex(ord(c))[2:].zfill(2) for c in x])
    return toHex

first = "Hi There"
second = "The ones"
key = "THEKEYZz"

# ciphertexts (in hex format)
c1 = toHex(strxor(first, key))
ciphers = [c1]
# The target ciphertext we want to crack
target_cipher = toHex(strxor(second, key))

both = toHex(strxor(c1.decode('hex'), target_cipher.decode('hex')))
print c1
print target_cipher
print both

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz "

attackLetters = []
locationLetters = []
possibleKeys = []

for letter in alpha:
    # is the character within our cipher?
    if toHex(letter) in c1: 
        # is the hex value in the correct spot?
        if c1.index(toHex(letter)) % 2 == 0:
            attackLetters.append(toHex(letter))
            locationLetters.append(c1.index(toHex(letter)) / 2)
            
    # is the character within our cipher?
    if toHex(letter) in target_cipher:   
        # is the hex value in the correct spot?
        if target_cipher.index(toHex(letter)) % 2 == 0:
            attackLetters.append(toHex(letter))
            locationLetters.append(target_cipher.index(toHex(letter)) / 2)

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
    print "At location: " + str(locationLetters[count])
    print 
    count +=1
