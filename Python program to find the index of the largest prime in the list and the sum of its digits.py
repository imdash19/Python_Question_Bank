# Write a Python program to find the index of the largest prime in the list and the sum of its digits.
# Input: [3, 7, 4]
# Output: [1, 7]
# Input: [3, 11, 7, 17, 19, 4]
# Output: [4, 10]
# Input: [23, 17, 201, 14, 10473, 43225, 421, 423, 11, 10, 2022, 342157]
# Output: [6, 7]

lst = eval(input())

def isprime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = []

for i in range(len(lst)):
    if isprime(lst[i]):
        primes.append((lst[i], i))

mx = max(primes)

num = mx[0]
idx = mx[1]

s = 0
for d in str(num):
    s += int(d)

print([idx, s])