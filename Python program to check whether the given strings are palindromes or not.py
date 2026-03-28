# Write a Python program to check whether the given strings are palindromes or not. Return True otherwise False.
# Input:
# ['palindrome', 'madamimadam', '', 'foo', 'eyes']
# Output:
# [False, True, True, False, False]

lst = eval(input())

result = []
for s in lst:
    result.append(s == s[::-1])

print(result)