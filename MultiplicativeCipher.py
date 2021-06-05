#!/usr/bin/env python3
"""
Simple file that can encode or decode a string using a Multiplicative cipher technique
Makes use of the English alphabet, sSo A = 0, Z = 25
"""

__author__ = "ScottishGuy95"
__license__ = "MIT"

# Alphabet using both upper and lower case letters
alphabet = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12,
            'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24,
            'Z': 25}


# 'a': 26, 'b': 27, 'c': 28, 'd': 29, 'e': 30, 'f': 31, 'g': 32, 'h': 33, 'i': 34, 'j': 35, 'k': 36, 'l': 37,
# 'm': 38, 'n': 39, 'o': 40, 'p': 41, 'q': 42, 'r': 43, 's': 44, 't': 45, 'u': 46, 'v': 47, 'w': 48, 'x': 49,
# 'y': 50, 'z': 51}


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
            result = (alphabet.get(text[x].upper()) * key) % len(alphabet)
            cipher += getKey(result)  # Gets the new character using the formula result
        else:  # All other possible characters are added as is
            cipher += text[x]
    return cipher


def valid_key(key):
    '''
    Used to verify if the given key is valid, by testing the alphabet against the key
    :param key: (int) The cipher key being tested
    :return: (boolean) Whether or not the given key works as a key for the multiplicative cipher
    '''
    text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cipher = encrypt(key, text)  # Returns the cipher text to be tested for duplicate characters
    if check_unique(cipher):  # Returns True if there are no duplicate characters
        return True
    return False


def check_unique(str):
    '''
    Used to check if a given key results in a one-to-one mapping, making it a valid key for the cipher
    :param str: (str) The result of the cipher that is being checked for duplicate characters
    :return: (boolean) Whether or not the given string is full of unique characters
    '''
    for i in range(len(str)):
        for j in range(i + 1, len(str)):
            if str[i] == str[j]:
                return False
    return True


def decrypt(key, cipher):
    # Greatest common divider
    pass


# Example variables
# TODO: Replace with user input
key = 1
text = 'Hello World'
cipher = 'xCzzU yUpzv'

test = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
uniques = []

# Testing how to test for valid keys
for x in range(100):
    # print('Multiplicative Cipher with key {}'.format(x))
    # print('Text = {}'.format(test))
    print("Testing if key {} is unique".format(x))
    if valid_key(x):
        uniques.append([x])
        cipher = encrypt(x, "hello world")
        print('\tVALID - Key {},Cipher = {}'.format(x, cipher))

    # print("Cipher all unique (1-1 mapping): " + str())
    # print("\n")

print("Unique keys:")
print(uniques)
# Get user input
# Check if key is valid
# Call encrypt method or decrpyt method
