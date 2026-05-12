# Write a program to encrypt strings using Caesar cipher logic.
# The program should accept space-separated strings from the user.
# Encryption rule:
# Each character is shifted by 1 position in the ASCII table.
# Python’s built-in map() function must be used.
# The program should use ord() and chr() for ASCII conversions.
# The output should be the encrypted strings.

def encrypt(word):
    return ''.join(map(lambda ch: chr(ord(ch) + 1), word))

strings = input("Enter space-separated strings: ").split()

encrypted = list(map(encrypt, strings))

print(encrypted)
