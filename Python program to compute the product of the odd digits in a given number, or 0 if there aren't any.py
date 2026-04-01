# Write a Python program to compute the product of the odd digits in a given number, or 0 if there aren't any.
# Input: 123456789
# Output:
# 945
# Input: 2468
# Output:
# 0
# Input: 13579
# Output:
# 945

n= int(input())
odd_prod= 1
result= False

while n!= 0:
    if (n%10) % 2 == 1:
        result= True
        odd_prod*= n%10
    n//= 10

print(odd_prod if result else 0)