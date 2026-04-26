# Write a Python program to capitalize the first and last letters of each word in a given string.

s = input()

words = s.split()
result = []

for w in words:
    if len(w) == 1:
        result.append(w.upper())
    else:
        result.append(w[0].upper() + w[1:-1] + w[-1].upper())

print(" ".join(result))