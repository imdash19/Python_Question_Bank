# Write a Python program to compute the largest product of three integers from a given list of integers.
# Sample Input:
# [-10, -20, 20, 1]
# [-1, -1, 4, 2, 1]
# [1, 2, 3, 4, 5, 6]
# Sample Output:
# 4000
# 8
# 120

a=list(map(int,input().strip('[]').split(',')))
a.sort()
p1=a[-1]*a[-2]*a[-3]
p2=a[0]*a[1]*a[-1]
print(max(p1,p2))