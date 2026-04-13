# Write a Python program to find the closest palindrome to a given string.
# Input: cat
# Output: cac
# Input: madan
# Output: madam
# Input: radivider
# Output: radividar
# Input: madan
# Output: madam
# Input: abc
# Output: aba
# Input: racecbr
# Output: racecar

s = input().strip()
s = list(s)

i = 0
j = len(s) - 1

while i < j:
    if s[i] != s[j]:
        s[j] = s[i]
    i += 1
    j -= 1

print("".join(s))