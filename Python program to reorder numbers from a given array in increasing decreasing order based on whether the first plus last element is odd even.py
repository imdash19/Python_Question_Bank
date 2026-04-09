# Write a Python program to reorder numbers from a given array in increasing/decreasing order based on whether the first plus last element is odd/even.
# Reorder numbers of a give array in increasing/decreasing order based on whether the first plus last element is odd/even.:
# Input: [3, 7, 4]
# Output: [3, 4, 7]
# Input: [2, 7, 4]
# Output: 7, 4, 2]
# Input: [1, 5, 6, 7, 4, 2, 8]
# Output: [1, 2, 4, 5, 6, 7, 8]
# Input: [1, 5, 6, 7, 4, 2, 9]
# Output: [9, 7, 6, 5, 4, 2, 1]

lst = eval(input())

if (lst[0] + lst[-1]) % 2 == 0:
    print(sorted(lst, reverse=True))
else:
    print(sorted(lst))