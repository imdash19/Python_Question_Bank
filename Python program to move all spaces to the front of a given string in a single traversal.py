# Write a Python program to move all spaces to the front of a given string in a single traversal.

s = input()

spaces = 0
result = ""

for ch in s:
    if ch == ' ':
        spaces += 1
    else:
        result += ch

print(' ' * spaces + result)