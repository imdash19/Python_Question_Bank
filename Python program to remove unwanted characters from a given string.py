# Write a Python program to remove unwanted characters from a given string.
# Sample Output:
# Original String : Pyth*^on Exercis^es
# After removing unwanted characters:
# Python Exercises
# Original String : A%^!B#*CD
# After removing unwanted characters:
# ABCD

import re

def clean_string(s):
    return re.sub(r'[^A-Za-z ]', '', s)

s = input()
print("Original String :", s)
print("After removing unwanted characters:")
print(clean_string(s))