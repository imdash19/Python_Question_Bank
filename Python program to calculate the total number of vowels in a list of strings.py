# Write a Python program to calculate the total number of vowels in a list of strings.
# The program should ask the user to enter a list of strings, separated by commas.
# For each string, count the number of vowels (a, e, i, o, u) in both uppercase and lowercase.
# Use Python’s functools.reduce() function to sum the counts from all strings.
# Finally, display the total number of vowels as a single integer.

from functools import reduce

strings = input("Enter strings separated by commas: ").split(",")

vowels = "aeiouAEIOU"

total_vowels = reduce(
    lambda total, s: total + sum(1 for ch in s if ch in vowels),
    strings,
    0
)

print("Total number of vowels:", total_vowels)
