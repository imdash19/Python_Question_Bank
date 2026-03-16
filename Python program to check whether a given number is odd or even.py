# Write a Python program to check whether a given number is odd or even.
# A number is called "Oddish" if the sum of all of its digits is odd, and a number is called "Evenish" if the sum of all of its digits is even.
# Sample Output:
# Original Number 120
# Check whether the sum of all digits of the said number is odd or even!
# Oddish
# Original Number 321
# Check whether the sum of all digits of the said number is odd or even!
# Evenish
# Original Number 43
# Check whether the sum of all digits of the said number is odd or even!
# Oddish
# Original Number 4433
# Check whether the sum of all digits of the said number is odd or even!
# Evenish
# Original Number 373
# Check whether the sum of all digits of the said number is odd or even!
# Oddish

n=int(input())
s=0
t=n
while n>0:
    s+=n%10
    n//=10
print("Original Number",t)
print("Check whether the sum of all digits of the said number is odd or even!")
if s%2==0:
    print("Evenish")
else:
    print("Oddish")