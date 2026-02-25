# Write a Python program that generates a list of all possible permutations from a given collection of distinct numbers.

from itertools import permutations

nums = list(map(int, input("Enter distinct numbers separated by space: ").split()))

perm_list = list(permutations(nums))

print("\nAll Possible Permutations:\n")
for p in perm_list:
    print(p)

print("\nTotal number of permutations:", len(perm_list))