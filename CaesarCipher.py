#!/usr/bin/env python3
"""
Simple file that can encode or decode a string using a Caesar cipher technique
"""

__author__ = "ScottishGuy95"
__license__ = "MIT"

# Imports
from itertools import cycle, islice
import sys


def caesar(character, shift, direction):
    """
    Replaces a given character by another a fixed number of positions down the alphabet (using the shift value)
    :param character: (str) The letter that will be encoded or decoded
    :param shift: (int) The number of characters to move along the alphabet
    :param direction: (str) Whether the character is being encoded or decoded
    :return: (str) The letter that has been encoded or decoded
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if direction == "decode":
        alphabet = alphabet[::-1]
    pos = alphabet.index(character)
    # Cycles the alphabet infinitely until it reaches the character denoted by the shift value
    # Returns the last value only, as that is the actual value for the cipher
    return ''.join(islice(cycle(alphabet), pos, pos + shift + 1))[-1]


request = ""
shift = ""
result = ""
title = r"""
    ---------------
     Caesar Cipher
    ---------------
"""

print(title)
while request not in ["encode", "decode"]:
    request = input("Please enter either Encode or decode: ").lower()

print("Rules\n\tText can be any letter, number or symbol\n\tShift must be a number")
text = input("Text (The phrase/word): ")
while True:
    shift = input("Shift (Number of positions to move): ")
    # Ensures that user input is a number and not too large or small
    if int(shift) >= sys.maxsize or int(shift) <= 0 or shift.isdigit() is False:
        print("\tMust be a number greater than 0 and less than %s" % sys.maxsize)
    else:
        break

# Loop through the given text, altering each letter
for ltr in text:
    if ltr.isalpha():                       # Used to pass the letters to the function
        # Passes the request value, so the function caesar_cipher knows to encode or decode
        result_ltr = caesar(ltr.lower(), int(shift), request)
        if ltr.isupper():                   # Ensures any capitalization is kept in correct place
            result += result_ltr.capitalize()
        else:
            result += result_ltr
    else:
        result += ltr                  # Adds any non-alpha characters as they are

print("Result: " + str(result))
