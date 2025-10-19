# Write a Python program to find the item with maximum occurrences in a given list.
# Original list: [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
# Item with maximum occurrences of the said list: 2

lst= [int(val) for val in input("Please enter your values separated with space: ").split()]
print('-'*60)
olst= []
for val in lst:
    olst.append(lst.count(val))
print("Original list: ", lst)
print('-'*60)
print("Item with maximum occurrences of the said list: ", lst[olst.index(max(olst))])