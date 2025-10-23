# Write a Python program to calculate the product of the unique numbers of a given list.
# Original List: [10, 20, 30, 40, 20, 50, 60, 40]
# Product of the unique numbers of the said list: 720000000

lst= [int(val) for val in input("Please enter your values separated with space: ").split()]
print("-"*60)
print("Original list= ", lst)
olst= []
for val in lst:
    if val not in olst:
        olst.append(val)
prod= 1
for val in olst:
    prod *= val
print("Product of the unique numbers of the said list: ", prod)