# Write a Python program to check whether the average value of the elements of a given array of numbers is a whole number or not.
# Original array:
# 1 3 5 7 9
# Check the average value of the elements of the said array is a whole number or not: True
# Original array:
# 2 4 2 6 4 8
# Check the average value of the elements of the said array is a whole number or not:
# False

arr = list(map(int, input().split()))
avg = sum(arr) / len(arr)
print(avg.is_integer())