# Write a program to find the product of all numbers in a flat list using recursion.
# User enters numbers space-separated.
# Each call multiplies first element with product of remaining list.
# Recursion stops when list has one element.
# Output is single integer.

def product_list(nums):
    if len(nums) == 1:
        return nums[0]
    
    return nums[0] * product_list(nums[1:])

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

print(product_list(numbers))
