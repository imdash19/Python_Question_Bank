# Write a Python program to check if a substring presents in a given list of string values.
# Original list: ['red', 'black', 'white', 'green', 'orange']
# Substring to search: ack
# Check if a substring presents in the said list of string values: True
# Substring to search: abc
# Check if a substring presents in the said list of string values: False

lst= [val for val in input("Please enter your values separated with space: ").split()]
print("-"*60)
print("Original list: ", lst)
print("-"*60)
sub= input("Please enter substring to search: ")
print("-"*60)
for val in lst:
    if sub in val:
        result= True
        break
    else:
        result= False
print("Check if a substring presents in the said list of string values: ", result)