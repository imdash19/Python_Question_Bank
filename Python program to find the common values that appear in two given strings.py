# Write a Python program to find the common values that appear in two given strings.
# Sample Output:
# Original strings:
# Python3
# Python2.7
# Intersection of two said String:
# Python

s1 = input()
s2 = input()
result = "".join(dict.fromkeys([c for c in s1 if c in s2]))
print(result)