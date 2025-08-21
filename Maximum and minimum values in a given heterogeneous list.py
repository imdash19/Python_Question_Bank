#   Write a PYTHON program to find the maximum and minimum values in a given heterogeneous list.
# 	Original list: ['PYTHON', 3, 2, 4, 5, 'version']
# 	Maximum and Minimum values in the said list: (5, 2)

lst = [val for val in input("Please enter your elements separated with sapce: ").split()]
print("-"*60)
olst = []
nlst = []
for val in lst:
    if val.isdigit():
        olst.append(int(val))
        nlst.append(int(val))
    else:
        olst.append(val)

print("Original list: ", olst)
print("-"*60)
print("Maximum and Minimum values in the said list: ({}, {})".format(max(nlst), min(nlst)))
print("-"*60)
print("Program executed successfully.")