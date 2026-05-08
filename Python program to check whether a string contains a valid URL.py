# Write a Python program to check whether a string contains a valid URL. 
# The program should accept a string input. 
# URLs start with http:// or https://. 
# Program should output True if URL exists, otherwise False.

import re

s = input()

pattern = r"https?://\S+"

if re.search(pattern, s):
    print(True)
else:
    print(False)
