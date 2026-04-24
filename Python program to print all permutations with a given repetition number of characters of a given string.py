# Write a Python program to print all permutations with a given repetition number of characters of a given string.

from itertools import product

s = input("Enter the string: ")
r = int(input("Enter repetition number: "))

perms = product(s, repeat=r)

for p in perms:
    print(''.join(p))