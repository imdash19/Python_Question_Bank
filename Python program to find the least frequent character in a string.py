# Write a Python program to find the least frequent character in a string. 
# The program should accept a string input. Ignore spaces.
# If multiple characters have same least frequency, display the first occurring one. 
# Case should be preserved. Output should be a single character.

s = input()
d = {}

for v in s:
    d[v] = s.count(v)

min_val = min(d.values())

for k, v in d.items():
    if v == min_val:
        print(k)
        break
