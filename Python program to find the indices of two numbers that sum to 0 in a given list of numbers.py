# Write a Python program to find the indices of two numbers that sum to 0 in a given list of numbers.
# Input:
# [1, -4, 6, 7, 4]
# Output:
# [4, 1]
# Input:
# [1232, -20352, 12547, 12440, 741, 341, 525, 20352, 91, 20]
# Output:
# [1, 7]

lst= [int(val) for val in input().split(', ') if (val.lstrip('-')).isdigit()]
i= []

for val1 in lst:
    for val2 in lst:
        if val1 + val2 == 0:
            i.append(lst.index(val2))
            i.append(lst.index(val1))
            break

print(list(set(i)))