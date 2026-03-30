# Write a Python program to compute the sum of the ASCII values of the upper-case characters in a given string.
# Input:
# PytHon ExerciSEs
# Output:
# 373
# Input:
# JavaScript
# Output:
# 157

s= input()
ASCII_sum= 0
for v in s:
    if v.isupper():
        ASCII_sum += ord(v)
print(ASCII_sum)