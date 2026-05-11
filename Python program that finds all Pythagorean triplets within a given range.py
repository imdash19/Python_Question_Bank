# Write a program that finds all Pythagorean triplets within a given range. The program takes one input: the upper limit of the range (starting from 1). A Pythagorean triplet is a set of three positive integers a, b, c such that a² + b² = c². Use Python's itertools.combinations_with_replacement to generate all possible combinations and check each one against the Pythagorean theorem condition. Display each valid triplet on a separate line in the format (a, b, c).
# Input Format: A single line containing the upper limit as an integer.
# Output Format: Multiple lines, each containing a valid Pythagorean triplet in the format (a, b, c), or no output if no triplets exist.

from itertools import combinations_with_replacement

def find_pythagorean_triplets(n):
    nums = range(1, n + 1)

    for a, b, c in combinations_with_replacement(nums, 3):
        if a**2 + b**2 == c**2:
            print((a, b, c))

if __name__ == "__main__":
    n = int(input())
    find_pythagorean_triplets(n)
