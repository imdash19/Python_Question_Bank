# Write a Python program to remove duplicate words from a given string.
# Sample Output:
# Original String:
# Python Exercises Practice Solution Exercises
# After removing duplicate words from the said string:
# Python Exercises Practice Solution

def remove_duplicates(s):
    words = s.split()
    seen = set()
    result = []
    for word in words:
        if word not in seen:
            seen.add(word)
            result.append(word)
    return " ".join(result)

s = input()
print("Original String:")
print(s)
print("After removing duplicate words from the said string:")
print(remove_duplicates(s))