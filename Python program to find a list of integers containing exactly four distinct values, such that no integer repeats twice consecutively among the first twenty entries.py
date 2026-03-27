# Write a Python program to find a list of integers containing exactly four distinct values, such that no integer repeats twice consecutively among the first twenty entries.
# Input:
# [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
# Output:
# True
# Input:
# [1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3]
# Output:
# False
# Input:
# [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
# Output:
# False

lst = list(map(int, input().strip('[]').split(',')))

if len(set(lst)) != 4:
    print(False)
else:
    res = True
    for i in range(1, min(20, len(lst))):
        if lst[i] == lst[i-1]:
            res = False
            break
    print(res)