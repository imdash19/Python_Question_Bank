# Write a Python program to find all integers <= 1000 that are the product of exactly three primes. Each integer should be represented as a list of its three prime factors.
# Input: 10
# Output: [[2, 2, 2]]
# Input: 50
# Output: [[2, 2, 2], [2, 2, 3], [2, 2, 5], [2, 2, 7], [2, 2, 11], [2, 3, 2], [2, 3, 3], [2, 3, 5], [2, 3, 7], [2, 5, 2], [2, 5, 3], [2, 5, 5], [2, 7, 2], [2, 7, 3], [2, 11, 2], [3, 2, 2], [3, 2, 3], [3, 2, 5], [3, 2, 7], [3, 3, 2], [3, 3, 3], [3, 3, 5], [3, 5, 2], [3, 5, 3], [3, 7, 2], [5, 2, 2], [5, 2, 3], [5, 2, 5], [5, 3, 2], [5, 3, 3], [5, 5, 2], [7, 2, 2], [7, 2, 3], [7, 3, 2], [11, 2, 2]]

n = int(input())

primes = []
for i in range(2, n+1):
    flag = 1
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            flag = 0
            break
    if flag:
        primes.append(i)

res = []

for i in primes:
    for j in primes:
        for k in primes:
            if i * j * k <= n:
                res.append([i, j, k])

print(res)