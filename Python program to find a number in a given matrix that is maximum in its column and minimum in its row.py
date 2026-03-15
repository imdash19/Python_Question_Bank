# Write a Python program to find a number in a given matrix that is maximum in its column and minimum in its row.
# Sample Input:
# Original matrix: [[1, 2], [2, 3]]
# Number in the said matrix which is maximum in its column and minimum in its row:
# [2]
# Original matrix: [[1, 2, 3], [3, 4, 5]]
# Number in the said matrix which is maximum in its column and minimum in its row:
# [3]
# Original matrix: [[7, 5, 6], [3, 4, 4], [6, 5, 7]]
# Number in the said matrix which is maximum in its column and minimum in its row:
# [5]

m = eval(input())

r = len(m)
c = len(m[0])
res = []

for i in range(r):
    row_min = min(m[i])
    col_index = m[i].index(row_min)

    col_max = m[0][col_index]
    for j in range(r):
        if m[j][col_index] > col_max:
            col_max = m[j][col_index]

    if row_min == col_max:
        res.append(row_min)

print(res)