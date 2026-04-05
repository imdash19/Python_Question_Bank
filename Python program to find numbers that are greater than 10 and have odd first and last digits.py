# Write a Python program to find numbers that are greater than 10 and have odd first and last digits.
# Input: [1, 3, 79, 10, 4, 1, 39, 62]
# Output: [79, 39]
# Input: [11, 31, 77, 93, 48, 1, 57]
# Output: [11, 31, 77, 93, 57]

lst = eval(input())

res = []

for x in lst:
    if x > 10:
        s = str(x)
        if int(s[0]) % 2 == 1 and int(s[-1]) % 2 == 1:
            res.append(x)

print(res)