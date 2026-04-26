# Write a Python program to compute the sum of the digits in a given string.

s = input()

total = 0

for ch in s:
    if ch.isdigit():
        total += int(ch)

print(total)