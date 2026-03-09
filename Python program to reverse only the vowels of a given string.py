# Write a Python program to reverse only the vowels of a given string.
# Sample Input:
# ("w3resource")
# ("Python")
# ("Perl")
# ("USA")
# Sample Output:
# w3resuorce
# Python
# Perl
# ASU

s = input().strip()

v = "aeiouAEIOU"
s = list(s)
i = 0
j = len(s) - 1

while i < j:
    if s[i] not in v:
        i += 1
    elif s[j] not in v:
        j -= 1
    else:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1

print("".join(s))