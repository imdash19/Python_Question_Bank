# Write a Python program to generate two strings from a given string. For the first string, use the characters that occur only once, and for the second, use the characters that occur multiple times in the said string.

s = input()

single = ""
multiple = ""

for ch in s:
    if s.count(ch) == 1:
        if ch not in single:
            single += ch
    else:
        if ch not in multiple:
            multiple += ch

print("Single occurrence characters:", single)
print("Multiple occurrence characters:", multiple)