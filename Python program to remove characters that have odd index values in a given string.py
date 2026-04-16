# Write a Python program to remove characters that have odd index values in a given string.

s = input('Please enter a string: ')
ns = ''

for i in range(len(s)):
    if i % 2 == 0:
        ns += s[i]

print(ns)