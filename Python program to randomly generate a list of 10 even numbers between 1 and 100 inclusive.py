# Write a Python program to randomly generate a list of 10 even numbers between 1 and 100 inclusive.
# Note: Use random.sample() to generate a list of random values.
# Sample Input:
# (1,100)
# Sample Output:
# [4, 22, 8, 20, 24, 12, 30, 98, 28, 48]

import random

a,b=map(int,input().strip("()").split(","))

even=[i for i in range(a,b+1) if i%2==0]

print(random.sample(even,10))