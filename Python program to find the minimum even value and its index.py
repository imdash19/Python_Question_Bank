# Given an array of numbers representing a branch on a binary tree, write a Python program to find the minimum even value and its index. In the case of a tie, return the smallest index. If there are no even numbers, the answer is [].
# Input:
# [1, 9, 4, 6, 10, 11, 14, 8]
# Output:
# Minimum even value and its index of the said array of numbers:
# [4, 2]
# Input:
# [1, 7, 4, 4, 9, 2]
# Output:
# Minimum even value and its index of the said array of numbers:
# [2, 5]
# Input:
# [1, 7, 7, 5, 9]
# Output:
# Minimum even value and its index of the said array of numbers:
# []

arr = list(map(int, input().strip('[]').split(',')))

min_even = float('inf')
min_index = -1

for i in range(len(arr)):
    if arr[i] % 2 == 0:
        if arr[i] < min_even:
            min_even = arr[i]
            min_index = i

if min_index == -1:
    print([])
else:
    print([min_even, min_index])