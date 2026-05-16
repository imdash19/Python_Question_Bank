# Write a program to remove all occurrences of a given character from a string using recursion.
# The program should compare the first character with the target character.
# If it matches, skip it. Otherwise include it in the result.
# Recursion continues until string becomes empty.

s, r= input(), input()

for v in s:
    if v != r:
        print(v, end= '')
