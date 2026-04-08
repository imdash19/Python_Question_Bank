# Given a list of numbers and a number to inject, write a Python program to create a list containing that number in between each pair of adjacent numbers.
# Input: [12, -7, 3, -89, 14, 88, -78, -1, 2, 7]
# Separator: 6
# Output: [12, 6, -7, 6, 3, 6, -89, 6, 14, 6, 88, 6, -78, 6, -1, 6, 2, 6, 7]
# Input: [1, 2, 3, 4, 5, 6]
# Separator: 9
# Output: [1, 9, 2, 9, 3, 9, 4, 9, 5, 9, 6]

lst= [int(val) for val in input('Please enter your values separated with space: ').split(', ')]
n= int(input('Please enter your separator value: '))
olst= [lst[0]]

for i in range(len(lst)-1):
    olst.append(n)
    olst.append(lst[i+1])

print(olst)