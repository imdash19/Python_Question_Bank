# Write a Python program to find the number which when appended to the list makes the total 0.
# Input: [1, 2, 3, 4, 5]
# Output: -15
# Input: [-1, -2, -3, -4, 5]
# Output: 5
# Input: [10, 42, 17, 9, 1315182, 184, 102, 29, 15, 39, 755]
# Output: -1316404

lst= [int(val) for val in input().split()]
plst= [val for val in lst if val >= 0]
nlst= [val for val in lst if val < 0]

res= sum(plst) + sum(nlst)
print(-1 * res)