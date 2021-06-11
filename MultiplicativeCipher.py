#!/usr/bin/env python3
"""
Simple file that can encode or decode a string using a Multiplicative cipher technique
Makes use of the English alphabet, so A = 0, Z = 25
"""

__author__ = "ScottishGuy95"
__license__ = "MIT"

# Imports
import math


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


def multiplicative(key, text, direction):
    """
    Used to return an encoded or decoded string of text using a multiplicative cipher
    :param key: (int) A value used to encode the key, must result in a 1-to-1 mapping.
    Requires the key to have no common divisor or be a multiple or the alphabet length.
    :param text: (str) The text being altered using the cipher
    :param direction: (str) "Encode" or "decode" depending on the users requirement
    :return: (str) The altered string for the user
    """
    # The alphabet linked to an int value from 0 to 25
    alphabet = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11,
                'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22,
                'X': 23, 'Y': 24, 'Z': 25}
    value = key
    result = ""
    for x in range(len(text)):                          # Loop through the given text, checking for letters
        # Decode by setting the using the original key to calculate the multiplicative inverse of the key
        # The use that value to return the ciphertext to the plaintext alternative
        # Otherwise encode using the key value to create the ciphertext
        if direction == "decode":
            value = pow(key, -1, len(alphabet))
        letter = (alphabet.get(text[x].upper()) * value) % len(alphabet)
        result += getKey(letter, alphabet)          # Gets the value responding to the given letter in the alphabet
    return result


title = r"""
    ---------------
     Multiplicative Cipher
    ---------------
"""
request = ""
key = ''

print(title)
while request not in ["encode", "decode"]:
    request = input("Please enter either encode or decode: ").lower()

print("Rules:\n\tText can be any letter, number or symbol\n\tKey must be a number")
text = input("Text (The phrase/word): ")
while True:
    key = input("Please enter a key value: ")

    # Used to verify that the given input has no common divider or a multiple or the alphabet length (26)
    if math.gcd(26, int(key)) != 1:
        print("\tInvalid key given")
    else:
        break

result = ""
# Pass each letter to be encoded/decoded to the cipher, to allow the original capitalisation to be kept or reset
for ltr in text:
    if ltr.isalpha():
        result_ltr = multiplicative(int(key), ltr, request)
        if ltr.isupper():
            result += result_ltr.capitalize()
        else:
            result += result_ltr.lower()
    else:
        result += ltr

print("Output: " + result)
