# Write a Python program to count Uppercase, Lowercase, special characters and numeric values in a given string.

s = input()

upper = 0
lower = 0
digit = 0
special = 0

for ch in s:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    elif ch.isdigit():
        digit += 1
    else:
        special += 1

print("Uppercase:", upper)
print("Lowercase:", lower)
print("Digits:", digit)
print("Special characters:", special)