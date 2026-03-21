# Write a Python program to convert the letters of a given string (same case-upper/lower) into alphabetical order.
# Original string: PHP
# Convert the letters of the said string into alphabetical order: HPP
# Original string: javascript
# Convert the letters of the said string into alphabetical order: aacijprstv
# Original string: python
# Convert the letters of the said string into alphabetical order: hnopty

s= list(input("Enter a string: "))
s.sort()
for v in s:
    print(v, end= '')