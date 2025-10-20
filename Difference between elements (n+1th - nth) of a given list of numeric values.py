# Write a Python program to find the difference between elements (n+1th - nth) of a given list of numeric values.
# Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Difference between elements (n+1th - nth) of the said list: [1, 1, 1, 1, 1, 1, 1, 1, 1]
# Original list: [2, 4, 6, 8]
# Difference between elements (n+1th - nth) of the said list: [2, 2, 2]

lst= [int(val) for val in input("Please enter your values separated with space: ").split()]
print("-"*60)
print("Original list: ", lst)
olst= []
for i in range(len(lst) - 1):
    o= lst[i+1] - lst[i]
    olst.append(o)
print("Difference between elements (n+1th - nth) of the said list: ", olst)