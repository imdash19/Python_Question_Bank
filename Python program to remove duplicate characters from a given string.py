# Write a Python program to remove duplicate characters from a given string.

s = input()

seen = set()
result = ""

for ch in s:
    if ch not in seen:
        seen.add(ch)
        result += ch

print(result)