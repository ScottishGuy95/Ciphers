#!/usr/bin/env python3
"""
Simple file that can encode or decode a string using a Multiplicative cipher technique
Makes use of the English alphabet (upper and lower case)
So A = 0, Z = 25, a = 26, z = 51
"""

__author__ = "ScottishGuy95"
__license__ = "MIT"

# Alphabet using both upper and lower case letters
alphabet = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12,
            'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24,
            'Z': 25,
            'a': 26, 'b': 27, 'c': 28, 'd': 29, 'e': 30, 'f': 31, 'g': 32, 'h': 33, 'i': 34, 'j': 35, 'k': 36, 'l': 37,
            'm': 38, 'n': 39, 'o': 40, 'p': 41, 'q': 42, 'r': 43, 's': 44, 't': 45, 'u': 46, 'v': 47, 'w': 48, 'x': 49,
            'y': 50, 'z': 51}


def getKey(num):
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


def encrypt(key, text):
    cipher = ''
    for x in range(len(text)):
        if text[x].isalpha():  # Used to only alter alphabetic characters
            # Formula = (alphabet number * key) mod (length of alphabet)
            # Alphabet number is taken from the dictionary value of each alphabetic character
            result = (alphabet.get(text[x]) * key) % len(alphabet)
            cipher += getKey(result)  # Gets the new character using the formula result
        else:  # All other possible characters are added as is
            cipher += text[x]
    return cipher


def decrypt(key, cipher):
    print('')


# Example variables
# TODO: Replace with user input
key = 7
text = 'Hello World'
cipher = 'xCzzU yUpzv'

print('Multiplicative Cipher with key {}'.format(key))
print('Text = {}'.format(text))
print('Cipher = {}'.format(encrypt(key, text)))
