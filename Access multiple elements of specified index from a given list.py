# Write a Python program to access multiple elements of specified index from a given list.
# Original list: [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
# Index list: [0, 3, 5, 7, 10]
# Items with specified index of the said list: [2, 4, 9, 2, 1]

lst= [int(val) for val in input("Please enter your values separated with space: ").split()]
print("-"*60)
idx= [int(val) for val in input("Please enter your index values separated with space: ").split()]
print("-"*60)
print("Original list: ", lst)
print("Index list: ",idx)
olst= []
for i in idx:
    op= lst[i]
    olst.append(op)
print("Items with specified index of the said list: ", olst)