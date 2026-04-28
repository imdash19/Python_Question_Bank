# Write a Python program to remove all characters except a specified character from a given string.
# Original string
# Python Exercises
# Remove all characters except P in the said string:
# P
# Original string
# google
# Remove all characters except g in the said string:
# gg
# Original string
# exercises
# Remove all characters except e in the said string:
# eee

s = input()
ch = input()

result = ""

for c in s:
    if c == ch:
        result += c

print(result if result else "No matching characters")