# Write a Python program to generate all permutations of a given string using inbuilt functions. 
# The program should accept a string input. 
# All unique orderings must be produced. 
# Output must list permutations clearly.

from itertools import permutations

s = input()

p = permutations(s)

for i in p:
    print("".join(i))
