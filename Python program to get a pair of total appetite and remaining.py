# For each triple of eaten, need, and stock, write a Python program to get a pair of total appetite and remaining.
# Input: [[2, 5, 6], [3, 9, 22]]
# Output: [[7, 1], [12, 13]]
# Input: [[2, 3, 18], [4, 9, 2], [2, 5, 7], [3, 8, 12], [4, 9, 106]]
# Output: [[5, 15], [6, 0], [7, 2], [11, 4], [13, 97]]
# Input: [[1, 2, 3], [4, 5, 6]]
# Output: [[3, 1], [9, 1]]

arr = eval(input())

res = []

for e, n, s in arr:
    total = e + n
    rem = s - total
    if rem < 0:
        rem = 0
    res.append([total, rem])

print(res)