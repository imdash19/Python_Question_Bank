# Write a Python program that adds up the columns and rows of the given table as shown in the specified figure.
# Input number of rows/columns (0 to exit)
# 4
# Input cell value:
# 25 69 51 26
# 68 35 29 54
# 54 57 45 63
# 61 68 47 59
# Result:
# 25 69 51 26 171
# 68 35 29 54 186
# 54 57 45 63 219
# 61 68 47 59 235
# 208 229 172 202 811
# Input number of rows/columns (0 to exit)

import sys

while True:
    n = int(input())
    if n == 0:
        break

    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    row_sums = [sum(row) for row in matrix]
    col_sums = [sum(matrix[i][j] for i in range(n)) for j in range(n)]
    total = sum(row_sums)

    print("Result:")
    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end=" ")
        print(row_sums[i])

    for j in range(n):
        print(col_sums[j], end=" ")
    print(total)