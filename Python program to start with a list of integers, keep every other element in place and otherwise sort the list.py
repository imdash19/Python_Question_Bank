# Write a Python program to start with a list of integers, keep every other element in place and otherwise sort the list.
# Input: [2, 5, 6, 3, 1, 4, 34]
# Output: [1, 5, 2, 3, 6, 4, 34]
# Input: [8, 0, 7, 2, 9, 4, 1, 2, 8, 3]
# Output: [1, 0, 7, 2, 8, 4, 8, 2, 9, 3]

lst = list(map(int, input().split()))

even_vals = sorted([lst[i] for i in range(0, len(lst), 2)])

j = 0
for i in range(0, len(lst), 2):
    lst[i] = even_vals[j]
    j += 1

print(lst)