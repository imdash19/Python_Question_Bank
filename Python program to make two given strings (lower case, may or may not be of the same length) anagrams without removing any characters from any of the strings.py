# Write a Python program to make two given strings (lower case, may or may not be of the same length) anagrams without removing any characters from any of the strings.

from collections import Counter

s1 = input().strip()
s2 = input().strip()

c1 = Counter(s1)
c2 = Counter(s2)

additions = 0

all_chars = set(c1.keys()) | set(c2.keys())

for ch in all_chars:
    additions += abs(c1.get(ch, 0) - c2.get(ch, 0))

print(additions)