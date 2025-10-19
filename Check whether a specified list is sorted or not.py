# Write a Python program to check whether a specified list is sorted or not.
# Original list: [1, 2, 4, 6, 8, 10, 12, 14, 16, 17]
# Is the said list is sorted!  True
# Original list: [1, 2, 4, 6, 8, 10, 15, 12, 14, 16, 17]
# Is the said list is sorted! False

lst= [int(val) for val in input("Please enter your values separated with space: ").split()]
if lst == sorted(lst):
    print("Is the said list is sorted!  ", True)
else:
    print("Is the said list is sorted!  ", False)