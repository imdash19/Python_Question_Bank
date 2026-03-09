# Write a Python program to check whether a given integer is a palindrome or not.
# Note: An integer is a palindrome when it reads the same backward as forward. Negative numbers are not palindromic.
# Sample Input:
# (100)
# (252)
# (-838)
# Sample Output:
# False
# True
# False

n = int(input())

if n < 0:
    print(False)
else:
    temp = n
    rev = 0
    while temp > 0:
        d = temp % 10
        rev = rev * 10 + d
        temp //= 10
    print(n == rev)