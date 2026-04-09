# Write a Python program to find the indices of three numbers that sum to 0 in a given list of numbers.
# Input: [12, -7, 3, -89, 14, 4, -78, -1, 2, 7]
# Output: [1, 2, 5]
# Input: [1, 2, 3, 4, 5, 6, -7]
# Output: [2, 3, 6]

lst = list(map(int, input().split(', ')))

n = len(lst)

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if lst[i] + lst[j] + lst[k] == 0:
                print([i, j, k])
                exit()

print(None)