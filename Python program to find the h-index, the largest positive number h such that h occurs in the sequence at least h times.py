# Write a Python program to find the h-index, the largest positive number h such that h occurs in the sequence at least h times. If there is no such positive number return h = -1.
# Input:
# [1, 2, 2, 3, 3, 4, 4, 4, 4]
# Output:
# 4
# Input:
# [1, 2, 2, 3, 4, 5, 6]
# Output:
# 2
# Input:
# [3, 1, 4, 17, 5, 17, 2, 1, 41, 32, 2, 5, 5, 5, 5]
# Output:
# 5

arr = list(map(int, input().strip('[]').split(',')))

freq = {}

for num in arr:
    if num > 0:
        freq[num] = freq.get(num, 0) + 1

h_index = -1

for num in freq:
    if freq[num] >= num:
        h_index = max(h_index, num)

print(h_index)