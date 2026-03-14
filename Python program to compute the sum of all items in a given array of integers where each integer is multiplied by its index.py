# Write a Python program to compute the sum of all items in a given array of integers where each integer is multiplied by its index. Return 0 if there is no number.
# Sample Input:
# [1,2,3,4]
# [-1,-2,-3,-4]
# []
# Sample Output:
# 20
# -20
# 0

s = input().strip()

if s == "[]":
    print(0)
else:
    a = list(map(int, s.strip('[]').split(',')))
    total = 0
    for i in range(len(a)):
        total += a[i] * i
    print(total)