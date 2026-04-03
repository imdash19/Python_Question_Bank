# Write a Python program to find the set of distinct characters in a given string, ignoring case.
# Input: HELLO
# Output:
# ['h', 'o', 'l', 'e']
# Input: HelLo
# Output:
# ['h', 'o', 'l', 'e']
# Input: Ignoring case
# Output:
# ['s', 'n', 'c', 'o', 'e', 'i', 'r', 'g', 'a', ' ']

s = input().lower()
result = list(set(s))
print(result)