#!/usr/bin/env python3
"""
Simple file that can encode or decode a string using a Affine cipher technique
Uses a combination of the logic from a Caesar Cipher and Multiplicative Cipher
"""

__author__ = "ScottishGuy95"
__license__ = "MIT"

# Imports
import sys
import math


def getModularInverse(key, alphabet_length):
    '''
    Uses the 'extended euclidean algorithm' to get a numbers modular inverse
    :param alphabet_length: (int) Length of the given alphabet
    :param key: (int) The number used to find its modular inverse
    :return: (int) The modular inverse of a given number
    '''
    u1, u2, u3 = 1, 0, key
    v1, v2, v3 = 0, 1, alphabet_length
    while v3 != 0:
        q = u3 // v3  # Integer division
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % alphabet_length


def getKey(num, alphabet):
    '''
    Used to return the alphabetic character of the given number, from the alphabet
    :param num: (int) The number as a result of the encryption formula
    :return: (str) The letter associated to the alphabet using the given number
    '''
    # Loops through the alphabet and compares the value of each element, against the given number
    # Returning the dictionary key when a match is found
    for k, v in alphabet.items():
        if v == num:
            return k


def affine(key_a, key_b, text, direction):
    '''
    Used to encode or decode a given string of text using the Affine Cipher
    :param key_a: (int) The first secret key
    :param key_b: (int) The second secret key
    :param text: (str) The text that will be altered
    :param direction: (str) Encode or decode from the users input
    :return: (str) The result of the affine cipher
    '''
    # a = key_a, b = key_b, m = alphabet length, p = value of the plaintext letter, c = value of the cipher letter
    # Encode formula: cipher = ap + b mod m
    # Decode formula: plaintext = (c - b) * inverse(a) mod m
    alphabet = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11,
                'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22,
                'X': 23, 'Y': 24, 'Z': 25}
    result = ""
    if direction == 'decode':
        # Get the inverse of key_a
        # Subtract key_b from the value of the given letter
        # and multiply that by the inverse then mod by the alphabet length
        inverse = getModularInverse(key_a, len(alphabet))
        value = (alphabet.get(text.upper()) - key_b) * inverse % len(alphabet)
    else:
        # Encode the plaintext by multiplying the first key with the value of the given letter from the alphabet
        # This is the multiplicative cipher
        # By adding key_b, we make use of the Cesar Cipher, which we then get the mod of those results
        value = ((key_a * alphabet.get(text.upper()) + key_b) % len(alphabet))
    # Get the alphabetic character using the encoded or decoded value, and return it
    result += getKey(value, alphabet)
    return result


title = r"""
    ---------------
     Affine Cipher
    ---------------
"""
request = ""
result = ""

print(title)
while request not in ["encode", "decode"]:
    request = input("Please enter either encode or decode: ").lower()

print("Rules:\n\tText can be any letter, number or symbol\n\tKeys must be numbers\n\tThe 2 key numbers used to encode, "
      "are required to decode the text, do not forget them")
text = input("Text (The phrase/word): ")

# Get a valid key from the user
while True:
    key_a = input("Please enter the value for key a: ")

    # Used to verify that the given input has no common divider or a multiple or the alphabet length (26)
    if math.gcd(26, int(key_a)) != 1:
        print("\tInvalid key given. Key must be relatively prime with the alphabet length (26)")
    else:
        break

# Get the second valid key from the user
while True:
    key_b = input("Please enter the value for key b: ")

    # Used to verify the given key_b value is a number and in the correct range of valid inputs
    if int(key_b) >= sys.maxsize or int(key_b) <= 0 or key_b.isdigit() is False:
        print("\tKey b be a number greater than 0 and less than %s" % sys.maxsize)
    else:
        break

# Pass each letter from the user to the cipher and return the results
# This allows the original capitalisation of each letter in the given text to be kept or reset per users request
for ltr in text:
    print(ltr)
    if ltr.isalpha():
        # Encrypt or decode the given letter
        result_ltr = affine(int(key_a), int(key_b), ltr, request)
        if ltr.isupper():
            result += result_ltr.capitalize()
        else:
            result += result_ltr.lower()
    else:
        result += ltr

print("Output: " + result)
