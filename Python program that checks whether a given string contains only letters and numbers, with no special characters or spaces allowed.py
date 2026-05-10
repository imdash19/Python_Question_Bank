# Write a program that checks whether a given string contains only letters and numbers, with no special characters or spaces allowed. The program should accept any string from the user and determine if it consists exclusively of alphabetic characters (A-Z, a-z) and numeric digits (0-9). Any presence of spaces, punctuation marks, symbols, or special characters should make the string invalid.
# You will use regular expressions with the re.fullmatch() function to perform this validation. This ensures that every character in the string, from the first to the last, meets the alphanumeric requirement without any exceptions.
# Input Format:

# A single line containing a string to be validated

# Output Format:

# Print "Valid alphanumeric string" if the string contains only letters and digits
# Print "Invalid string" if the string contains any special characters, spaces, or is empty

import re

s = input()

if re.fullmatch(r"[A-Za-z0-9]+", s):
    print("Valid alphanumeric string")
else:
    print("Invalid string")
