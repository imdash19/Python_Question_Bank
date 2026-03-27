# Write a Python program to check a given list of integers where the sum of the first i integers is i.
# Input:
# [0, 1, 2, 3, 4, 5]
# Output:
# False
# Input:
# [1, 1, 1, 1, 1, 1]
# Output:
# True
# Input:
# [2, 2, 2, 2, 2]
# Output:
# False

lst = [int(val) for val in input().split()]

res = True
s = 0

for i in range(1, len(lst) + 1):
    s += lst[i-1]
    if s != i:
        res = False
        break

print(res)