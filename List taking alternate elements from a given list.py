# Write a Python program to create a list taking alternate elements from a given list.
# Original list: ['red', 'black', 'white', 'green', 'orange']
# List with alternate elements from the said list: ['red', 'white', 'orange']
# Original list: [2, 0, 3, 4, 0, 2, 8, 3, 4, 2]
# List with alternate elements from the said list: [2, 3, 0, 8, 4]

lst= [val for val in input("Please enter your values separated with space: ").split()]
print("-"*60)
print("Original list: ", lst)
for val in lst:
    try:
        lst.pop(lst.index(val)+1)
    except IndexError:
        res= lst
    else:
        res= lst
print("List with alternate elements from the said list: ", res)