# Write a Python program to calculate Euclid's totient function for a given integer. Use a primitive method to calculate Euclid's totient function.
# Sample Input:
# (10)
# (15)
# (33)
# Sample Output:
# 4
# 8
# 20

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def totient(n):
    count = 0
    for i in range(1, n):
        if gcd(i, n) == 1:
            count += 1
    return count

t = int(input())
for _ in range(t):
    n = eval(input())
    print(totient(n))