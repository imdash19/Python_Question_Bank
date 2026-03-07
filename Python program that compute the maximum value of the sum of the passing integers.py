# Arrange integers (0 to 99) as narrow hilltop, as illustrated in Figure 1. Reading such data representing huge, when starting from the top and proceeding according to the next rule to the bottom. Write a Python program that compute the maximum value of the sum of the passing integers.
# Input: A series of integers separated by commas are given in diamonds. No spaces are included in each line. The input example corresponds to Figure 1. The number of lines of data is less than 100 lines.
# Output: The maximum value of the sum of integers passing according to the rule on one line.
# Input the numbers (ctrl+d to exit):
# 8
# 4, 9
# 9, 2, 1
# 3, 8, 5, 5
# 5, 6, 3, 7, 6
# 3, 8, 5, 5
# 9, 2, 1
# 4, 9
# 8
# Maximum value of the sum of integers passing according to the rule on one line.
# 64

import sys

rows = []

try:
    while True:
        line = input().strip()
        rows.append(list(map(int, line.split(","))))
except EOFError:
    pass

for i in range(len(rows)-2, -1, -1):
    for j in range(len(rows[i])):
        rows[i][j] += max(rows[i+1][j], rows[i+1][j+1])

print(rows[0][0])