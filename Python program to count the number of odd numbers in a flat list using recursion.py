# Write a program to count the number of odd numbers in a flat list using recursion.
# User enters numbers space-separated.
# Recursion checks first element: if odd, increments count.
# Continues recursively on remaining list.
# Output is single integer.

def count_odd(nums):
    if len(nums) == 0:
        return 0
    
    if nums[0] % 2 != 0:
        return 1 + count_odd(nums[1:])
    else:
        return count_odd(nums[1:])

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

print(count_odd(numbers))
