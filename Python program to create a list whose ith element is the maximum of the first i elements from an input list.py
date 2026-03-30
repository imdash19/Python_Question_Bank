# Write a Python program to create a list whose ith element is the maximum of the first i elements from an input list.
# Input:
# [0, -1, 3, 8, 5, 9, 8, 14, 2, 4, 3, -10, 10, 17, 41, 22, -4, -4, -15, 0]
# Output:
# [0, 0, 3, 8, 8, 9, 9, 14, 14, 14, 14, 14, 14, 17, 41, 41, 41, 41, 41, 41]
# Input:
# [6, 5, 4, 3, 2, 1]
# Output:
# [6, 6, 6, 6, 6, 6]
# Input:
# [1, 19, 5, 15, 5, 25, 5]
# Output:
# [1, 19, 19, 19, 19, 25, 25]

lst= [int(val) for val in input().split()]
olst= []
max= lst[0]

for val in lst:
    if val < max:
        olst.append(max)
    else:
        max= val
        olst.append(max)

print(olst)