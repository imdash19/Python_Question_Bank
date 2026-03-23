# Write a Python program to find the closest palindrome number to a given integer. If there are two palindrome numbers in absolute distance return the smaller number.
# Original number: 120
# Closest Palindrome number of the said number: 121
# Original number: 321
# Closest Palindrome number of the said number: 323
# Original number: 43
# Closest Palindrome number of the said number: 44
# Original number: 1234
# Closest Palindrome number of the said number: 1221

n = int(input())

def is_pal(x):
    return str(x) == str(x)[::-1]

i = 0
while True:
    if n - i >= 0 and is_pal(n - i):
        print(n - i)
        break
    if is_pal(n + i):
        print(n + i)
        break
    i += 1