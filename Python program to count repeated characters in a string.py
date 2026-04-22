# Write a Python program to count repeated characters in a string.
# Sample string: 'thequickbrownfoxjumpsoverthelazydog'
# Expected output :
# o 4
# e 3
# u 2
# h 2
# r 2
# t 2

s=input('Enter your string: ')
lst= []
for v in s:
    if s.count(v) > 1 and v not in lst:
        lst.append(v)

for val in lst:
    print(val, s.count(val))