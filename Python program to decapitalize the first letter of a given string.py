# Write a Python program to decapitalize the first letter of a given string.
# Sample Output:
# java Script
# python

s = input()

if s:
    result = s[0].lower() + s[1:]
else:
    result = ""

print(result)