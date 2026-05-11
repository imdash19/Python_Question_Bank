# Write a program to remove special characters from strings. 
# The program should accept comma-separated strings from the user. 
# All special characters must be removed.
# Only alphabets and numbers should remain.
# Python’s map() function should be used.
# Regular expressions should be applied for cleaning text.

import re

def clean_text(s):
    return re.sub(r'[^A-Za-z0-9]', '', s)

if __name__ == "__main__":
    strings = input().split(',')

    result = list(map(clean_text, strings))

    print(result)
