# Write a Python program to find the indices of two entries that show that the list is not in increasing order. If there are no violations (they are increasing), return an empty list.
# Input:
# [1, 2, 3, 0, 4, 5, 6]
# Output:
# [2, 3]
# Input:
# [1, 2, 3, 4, 5, 6]
# Output:
# []
# Input:
# [1, 2, 3, 4, 6, 5, 7]
# Output:
# [4, 5]
# Input:
# [-3, -2, -3, 0, 2, 3, 4]
# Output:
# [1, 2]

arr = list(map(int, input().strip('[]').split(',')))

result = []

for i in range(len(arr) - 1):
    if arr[i] >= arr[i + 1]:
        result = [i, i + 1]
        break

print(result)