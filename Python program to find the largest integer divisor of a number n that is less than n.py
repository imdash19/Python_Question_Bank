# Write a Python program to find the largest integer divisor of a number n that is less than n.
# Input: 18
# Output:
# 9
# Input: 100
# Output:
# 50
# Input: 102
# Output:
# 51
# Input: 500
# Output:
# 250
# Input: 1000
# Output:
# 500
# Input: 6500
# Output:
# 3250

n= int(input())
lst= []

for i in range(1, n):
    if n % i == 0:
        lst.append(i)

print(lst[-1])