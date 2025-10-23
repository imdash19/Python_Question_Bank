# Write a Python program to reverse strings in a given list of string values.
# Original lists: ['Red', 'Green', 'Blue', 'White', 'Black']
# Reverse strings of the said given list: ['deR', 'neerG', 'eulB', 'etihW', 'kcalB']

lst= [val for val in input("Please enter your values separated with space: ").split()]
print("-"*60)
print("Original lists: ", lst)
olst= []
for val in lst:
    olst.append(val[::-1])
print("Reverse strings of the said given list: ", olst)