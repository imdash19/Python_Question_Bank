# Write a Python program to print a given N by M matrix of numbers line by line in forward > backwards > forward >... order.
# Input matrix:
# [[1, 2, 3,4],
# [5, 6, 7, 8],
# [0, 6, 2, 8],
# [2, 3, 0, 2]]
# Output:
# 1
# 2
# 3
# 4
# 8
# 7
# 6
# 5
# 0
# 6
# 2
# 8
# 2
# 0
# 3
# 2

n=int(input())
m=int(input())
matrix=[]
for i in range(n):
    row=list(map(int,input().split()))
    matrix.append(row)
for i in range(n):
    if i%2==0:
        for j in range(m):
            print(matrix[i][j])
    else:
        for j in range(m-1,-1,-1):
            print(matrix[i][j])