# Write a Python program to find the first negative balance from a given list of numbers that represent bank deposits and withdrawals.
# Input: [[12, -7, 3, -89, 14, 88, -78], [-1, 2, 7]]
# Output: [-81, -1]
# Input: [[1200, 100, -900], [100, 100, -2400]]
# Output: [None, -2200]

lst= [[int(val) for val in input('Enter your values separated with space: ').split()] for i in range(2)]
olst= []
for val in lst:
    temp= 0
    for v in val:
        temp+= v
        if temp < 0:
            olst.append(temp)
            break
    else:
        olst.append(None)

print(olst)