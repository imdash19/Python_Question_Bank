# Write a Python program to sort the numbers in a given list by the sum of their digits.
# Input: [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# Output:
# [10, 11, 20, 12, 13, 14, 15, 16, 17, 18, 19]
# Input: [23, 2, 9, 34, 8, 9, 10, 74]
# Output:
# [10, 2, 23, 34, 8, 9, 9, 74]

def digit_sum(n):
    s = 0
    while n != 0:
        s += n % 10
        n //= 10
    return s

lst = [int(val) for val in input().split()]

if lst:
    result = sorted(lst, key=digit_sum)
    print(result)