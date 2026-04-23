# Write a Python program to check whether a string contains all letters of the alphabet.

import string

text = input("Enter a string: ").lower()

alphabet = set(string.ascii_lowercase)
text_set = set(text)

if alphabet.issubset(text_set):
    print("The string contains all letters of the alphabet.")
else:
    print("The string does NOT contain all letters of the alphabet.")