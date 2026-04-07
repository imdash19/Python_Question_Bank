# Write a Python program to find the indices of the closest pair from a list of numbers.
# Input: [1, 7, 9, 2, 10]
# Output: [0, 3]
# Input: [1.1, 4.25, 0.79, 1.0, 4.23]
# Output: [4, 1]
# Input: [0.21, 11.3, 2.01, 8.0, 10.0, 3.0, 15.2]
# Output: [2, 5]

def closest_pair_indices(arr):
    min_diff = float('inf')
    idx1, idx2 = 0, 0

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            diff = abs(arr[i] - arr[j])
            if diff < min_diff:
                min_diff = diff
                idx1, idx2 = i, j

    return [idx1, idx2]

arr = eval(input())
print(closest_pair_indices(arr))