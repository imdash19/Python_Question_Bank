# Write a Python program to count the number of non-empty substrings of a given string.

s = input().strip()
n = len(s)
print(n * (n + 1) // 2)