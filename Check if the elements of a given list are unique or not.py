# Write a Python program to check if the elements of a given list are unique or not.
# Original list: [1, 2, 4, 6, 8, 2, 1, 4, 10, 12, 14, 12, 16, 17]
# Is the said list containing all unique elements! False
# Original list: [2, 4, 6, 8, 10, 12, 14]
# Is the said list containing all unique elements! True

lst= [int(val) for val in input("Please enter your values separated with space: ").split()]
print("-"*60)
olst= []
for val in lst:
    if val in olst:
        result= False
        break
    else:
        olst.append(val)
        result= True
print("Is the said list containing all unique elements! ", result)