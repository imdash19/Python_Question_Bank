# Write a Python program to accept strings that contain all vowels (a, e, i, o, u).
# The program should check each input string.
# Case should be ignored. Spaces or special characters should not affect vowel check.
# If all vowels exist, print the string; otherwise, skip(Empty). Output should list only valid strings.

s= input()
temp= []

for v in s:
    if v in 'aeiou' and v not in temp:
        temp.append(v)

temp.sort()
if temp == ['a', 'e', 'i', 'o', 'u']:
    print(s)
