# Write a Python program to find the first missing positive integer that does not exist in a given list.
# Sample Input:
# [2, 3, 7, 6, 8, -1, -10, 15, 16]
# [1, 2, 4, -7, 6, 8, 1, -10, 15]
# [1, 2, 3, 4, 5, 6, 7]
# [-2, -3, -1, 1, 2, 3]
# Sample Output:
# 4
# 3
# 8
# 4

a=list(map(int,input().strip('[]').split(',')))
s=set(a)
i=1
while True:
    if i not in s:
        print(i)
        break
    i+=1