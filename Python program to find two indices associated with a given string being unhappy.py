# A string is happy if every three consecutive characters are distinct. Write a Python program to find two indices associated with a given string being unhappy.
# Input: Python
# Output: None
# Input: Unhappy
# Output: [4, 5]
# Input: Find
# Output: None
# Input: Street
# Output: [3, 4]

s = input().strip()

res = None

for i in range(len(s) - 2):
    if s[i] == s[i+1] or s[i] == s[i+2] or s[i+1] == s[i+2]:
        res = [i+1, i+2]
        break

print(res)