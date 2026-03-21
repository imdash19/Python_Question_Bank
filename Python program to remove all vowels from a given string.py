# Write a Python program to remove all vowels from a given string.
# Original string: Python
# After removing all the vowels from the said string: Pythn
# Original string: C Sharp
# After removing all the vowels from the said string: C Shrp
# Original string: JavaScript
# After removing all the vowels from the said string: JvScrpt

s= list(input())
ns= ''
for v in s:
    if v.lower() not in 'aeiou':
        ns+= v

print(ns)