# Write a Python program to convert all items in a given list to float values.
# Original list:
# ['0.49', '0.54', '0.54', '0.54', '0.54', '0.54', '0.55', '0.54', '0.54', '0.54', '0.55', '0.55', '0.55', '0.54', '0.55', '0.55', '0.54', '0.55', '0.55', '0.54']
# List of Floats:
# [0.49, 0.54, 0.54, 0.54, 0.54, 0.54, 0.55, 0.54, 0.54, 0.54, 0.55, 0.55, 0.55, 0.54, 0.55, 0.55, 0.54, 0.55, 0.55, 0.54]

lst = eval(input())
res = [float(i) for i in lst]
print(res)