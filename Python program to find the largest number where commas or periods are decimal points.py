# Write a Python program to find the largest number where commas or periods are decimal points.
# Input:
# ['100', '102,1', '101.1']
# Output:
# 102.1

lst= [float(val.replace(',', '.')) for val in input().split()]
print(max(lst))