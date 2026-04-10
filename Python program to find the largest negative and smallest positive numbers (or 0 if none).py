# Write a Python program to find the largest negative and smallest positive numbers (or 0 if none).
# Input: [-12, -6, 300, -40, 2, 2, 3, 57, -50, -22, 12, 40, 9, 11, 18]
# Output: [-6, 2]
# Input: [-1, -2, -3, -4]
# Output: [-1, 0]
# Input: [1, 2, 3, 4]
# Output: [0, 1]
# Input: []
# Output: [0, 0]

lst= [int(val) for val in input('Please enter your values separated with space: ').split()]

nlst= [val for val in lst if val < 0]
nlst.sort()

plst= [val for val in lst if val > 0]
plst.sort()

if nlst and plst:
    print(nlst[-1], plst[0])

elif not nlst:
    print(0, plst[0])

elif not plst:
    print(nlst[-1], 0)

else:
    print(0, 0)