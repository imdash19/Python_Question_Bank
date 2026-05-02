# Write a Python program to extract numbers from a given string.
# Sample Output:
# Original string: red 12 black 45 green
# Extract numbers from the said string: [12, 45]

import re

s = input()
numbers = list(map(int, re.findall(r'\d+', s)))

print("Original string:", s)
print("Extract numbers from the said string:", numbers)