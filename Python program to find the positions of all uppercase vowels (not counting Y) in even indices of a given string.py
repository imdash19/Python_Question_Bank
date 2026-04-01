# Write a Python program to find the positions of all uppercase vowels (not counting Y) in even indices of a given string.
# Input: w3rEsOUrcE
# Output:
# [6]
# Input: AEIOUYW
# Output:
# [0, 2, 4]

s = input().strip()

vowels = "AEIOU"

res = [i for i in range(0, len(s), 2) if s[i] in vowels]

print(res)