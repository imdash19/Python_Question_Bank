# Write a Python program to determine the direction ('increasing' or 'decreasing') of monotonic sequence numbers.
# Input:
# [1, 2, 3, 4, 5, 6]
# Output:
# Increasing.
# Input:
# [6, 5, 4, 3, 2, 1]
# Output:
# Decreasing.
# Input:
# [19, 19, 5, 5, 5, 5, 5]
# Output:
# Not a monotonic sequence!

nums = eval(input())

if all(nums[i] < nums[i+1] for i in range(len(nums)-1)):
    print("Increasing.")
elif all(nums[i] > nums[i+1] for i in range(len(nums)-1)):
    print("Decreasing.")
else:
    print("Not a monotonic sequence!")