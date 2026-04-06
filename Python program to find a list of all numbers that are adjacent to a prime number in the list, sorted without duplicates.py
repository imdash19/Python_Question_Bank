# Write a Python program to find a list of all numbers that are adjacent to a prime number in the list, sorted without duplicates.
# Input: [2, 17, 16, 0, 6, 4, 5]
# Output: [2, 4, 16, 17]
# Input: [1, 2, 19, 16, 6, 4, 10]
# Output: [1, 2, 16, 19]
# Input: [1, 2, 3, 5, 1, 16, 7, 11, 4]
# Output: [1, 2, 3, 4, 5, 7, 11, 16]

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

lst = [int(val) for val in input().split()]

res = []

for i in range(len(lst)):
    if (i > 0 and is_prime(lst[i-1])) or (i < len(lst)-1 and is_prime(lst[i+1])):
        res.append(lst[i])

print(sorted(list(set(res))))