# Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'

s= input()
ns= s[0]
for c in s[1:]:
    if c == s[0]:
        ns+= '$'
    else:
        ns+= c
print(ns)