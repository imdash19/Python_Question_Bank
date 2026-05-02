# Write a Python program to find string similarity between two given strings.
# Sample Output:
# Original string:
# Python Exercises
# Python Exercises
# Similarity between two said strings:
# 1.0
# Original string:
# Python Exercises
# Python Exercise
# Similarity between two said strings:
# 0.967741935483871
# Original string:
# Python Exercises
# Python Ex.
# Similarity between two said strings:
# 0.6923076923076923
# Original string:
# Python Exercises
# Python
# Similarity between two said strings:
# 0.5454545454545454
# Original string:
# Java Exercises
# Python
# Similarity between two said strings:
# 0.0

from difflib import SequenceMatcher

def similarity(s1, s2):
    return SequenceMatcher(None, s1, s2).ratio()

s1 = input()
s2 = input()

print("Original string:")
print(s1)
print(s2)
print("Similarity between two said strings:")
print(similarity(s1, s2))