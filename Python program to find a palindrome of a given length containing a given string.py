# Write a Python program to find a palindrome of a given length containing a given string.
# Input: madam , 7
# Output: madaadam
# Input: madam , 6
# Output: maddam
# Input: madam , 5
# Output: maaaam
# Input: madam , 3
# Output: maam
# Input: madam , 2
# Output: mm
# Input: madam , 1
# Output: aa

s, n = input().split(',')
s = s.strip()
n = int(n)

res = [''] * n

i = 0
j = n - 1
k = 0

while i <= j:
    ch = s[k % len(s)]
    res[i] = ch
    res[j] = ch
    i += 1
    j -= 1
    k += 1

print("".join(res))