# Write a Python program to count the number of equal numbers from three given integers.
# Sample Input:
# (1, 1, 1)
# (1, 2, 2)
# (-1, -2, -3)
# (-1, -1, -1)
# Sample Output:
# 3
# 2
# 0
# 3

a=int(input("Enter first integer: "))
b=int(input("Enter second integer: "))
c=int(input("Enter third integer: "))

if a==b==c:
    print(3)
elif a==b or b==c or a==c:
    print(2)
else:
    print(0)