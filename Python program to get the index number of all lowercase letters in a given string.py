# Write a Python program to get the index number of all lowercase letters in a given string.
# Original string: Python
# Indices of all lowercase letters of the said string: [1, 2, 3, 4, 5] Original string: JavaScript
# Indices of all lowercase letters of the said string: [1, 2, 3, 5, 6, 7, 8, 9] Original string: PHP
# Indices of all lowercase letters of the said string: []

s = input()
res = []
for i in range(len(s)):
    if s[i].islower():
        res.append(i)
print(res)