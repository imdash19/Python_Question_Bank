# Write a Python program to remove all consecutive duplicates of a given string.

s = input().strip()

result = ""
for ch in s:
    if not result or result[-1] != ch:
        result += ch

print(result)