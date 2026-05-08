# Write a Python program to find the character with maximum frequency in a string. 
# The program should accept a string. Ignore spaces. 
# If multiple characters have same frequency, output the first occurring one. 
# Output should be a single character.

s = input()
d = {}

for v in s:
    d[v] = s.count(v)

max_val = max(d.values())

for k, v in d.items():
    if v == max_val:
        print(k)
        break
