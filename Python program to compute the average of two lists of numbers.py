# Write a Python program to compute the average of two lists of numbers.
# The program should ask the user to enter two space-separated lists of numbers.
# Convert the input into integers or floats.
# Use Python’s sum() and len() functions to compute the combined average of both lists.
# Display the result as a float.

lst1= list(map(int, input().split()))
lst2= list(map(int, input().split()))

print((sum(lst1) + sum(lst2))/(len(lst1) + len(lst2)))
