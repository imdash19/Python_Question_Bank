# Write a PYTHON program to extract common index elements from more than one given list.
# 	Original lists:
# 	[1, 1, 3, 4, 5, 6, 7]
# 	[0, 1, 2, 3, 4, 5, 7]
# 	[0, 1, 2, 3, 4, 5, 7]
# 	Common index elements of the said lists: [1, 7]

# Take number of lists
n = int(input("Enter number of lists: "))

lists = []
for i in range(n):
    lst = input("Enter elements of list {} separated by space: ".format(i+1)).split()
    lst = [int(x) for x in lst]   # convert to integers
    lists.append(lst)

min_len = min(len(lst) for lst in lists)

common = []
for i in range(min_len):
    # Check if all lists have the same element at index i
    first = lists[0][i]
    if all(lst[i] == first for lst in lists):
        common.append(first)

print("\nOriginal lists:")
for lst in lists:
    print(lst)

print("Common index elements of the said lists:")
print(common)