# Reads a string and validates that it contains only alphanumeric characters (letters and digits). The program checks for absence of special characters or whitespace.

text = input()

if text.isalnum():
    print("Valid")
else:
    print("Invalid")