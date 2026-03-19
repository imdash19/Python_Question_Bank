# Write a Python program to identify non-prime numbers between 1 and 100 (integers). Print the non-prime numbers.
# Sample Input:
# range(1, 101)
# Sample Output:
# Nonprime numbers between 1 to 100:
# 4
# 6
# 8
# 9
# 10
# ..
# 96
# 98
# 99
# 100

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

start, end = map(int, input().split())

print(f"Nonprime numbers between {start} to {end}:")
for i in range(start, end + 1):
    if not is_prime(i):
        print(i)