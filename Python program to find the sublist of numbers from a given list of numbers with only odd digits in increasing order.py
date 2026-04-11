# Write a Python program to find the sublist of numbers from a given list of numbers with only odd digits in increasing order.
# Input: [1, 3, 79, 10, 4, 2, 39]
# Output: [1, 3, 39, 79]
# Input: [11, 31, 40, 68, 77, 93, 48, 1, 57]
# Output: [1, 11, 31, 57, 77, 93]
# Input: [9, -2, 3, 4, -2, 0, 2, -3, 8, -1]
# Output: [-3, -1, 3, 9]

def only_odd_digits(n):
    n = abs(n)
    if n == 0:
        return False
    while n > 0:
        d = n % 10
        if d % 2 == 0:
            return False
        n //= 10
    return True

lst = list(map(int, input().strip('[]').split(',')))

res = [x for x in lst if only_odd_digits(x)]
res.sort()

print(res)