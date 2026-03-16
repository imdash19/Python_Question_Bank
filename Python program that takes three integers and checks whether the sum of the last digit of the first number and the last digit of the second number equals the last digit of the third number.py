# Write a Python program that takes three integers and checks whether the sum of the last digit of the first number and the last digit of the second number equals the last digit of the third number.
# Sample Input:
# (12, 26, 44)
# (145, 122, 1010)
# (0, 20, 40)
# (1, 22, 40)
# (145, 129, 104)
# Sample Output:
# True
# False
# True
# False
# True

a=int(input())
b=int(input())
c=int(input())
if (a%10 + b%10) % 10 == c%10:
    print(True)
else:
    print(False)