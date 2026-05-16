# Write a program to find the sum of squares of numbers in a flat list using recursion.
# User enters numbers space-separated.
# Each recursive call squares the first element and adds it to sum of remaining list. Output is single integer.

lst= [int(val)**2 for val in input().split()]
print(sum(lst))
