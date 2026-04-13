# Write a Python program to find the following strange sort of list of numbers: the first element is the smallest, the second is the largest of the remaining, the third is the smallest of the remaining, the fourth is the smallest of the remaining, etc.
# Input: [1, 3, 4, 5, 11]
# Output: [1, 11, 3, 5, 4]
# Input: [27, 3, 8, 5, 1, 31]
# Output: [1, 31, 3, 27, 5, 8]
# Input: [1, 2, 7, 3, 4, 5, 6]
# Output: [1, 7, 2, 6, 3, 5, 4]

lst= [int(val) for val in input('Please enter your values separated with space: ').split()]
lst.sort()
olst= []

while lst:
    if lst:
        olst.append(lst.pop(0))
    if lst:
        olst.append(lst.pop(-1))
    if lst:
        olst.append(lst.pop(0))
    if lst:
        olst.append(lst.pop(-1))

print(olst)