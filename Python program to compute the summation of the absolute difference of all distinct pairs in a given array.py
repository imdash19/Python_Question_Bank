# Write a Python program to compute the summation of the absolute difference of all distinct pairs in a given array (non-decreasing order).
# Sample array: [1, 2, 3]
# Then all the distinct pairs will be:
# 1 2
# 1 3
# 2 3

def sum_absolute_difference():
    arr = list(map(int, input("Enter elements in non-decreasing order (space-separated): ").split()))

    n = len(arr)
    total_sum = 0
    prefix_sum = 0

    for i in range(n):
        total_sum += arr[i] * i - prefix_sum
        prefix_sum += arr[i]

    print("\nSum of absolute differences of all distinct pairs:", total_sum)

sum_absolute_difference()