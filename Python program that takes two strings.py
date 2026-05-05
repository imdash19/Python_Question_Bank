# Write a Python program that takes two strings. Count the number of times each string contains the same three letters at the same index.
# Sample Data:
# ("Red RedGreen") -> 1
# ("Red White Red White) -> 7
# ("Red White White Red") -> 0

s1 = input()
s2 = input()

count = 0
min_len = min(len(s1), len(s2))

for i in range(min_len - 2):
    if s1[i:i+3] == s2[i:i+3]:
        count += 1

print(count)