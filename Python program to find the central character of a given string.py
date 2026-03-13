# Write a Python program to find the central character(s) of a given string. Return the two middle characters if the length of the string is even. Return the middle character if the length of the string is odd.
# Original string: Python
# Middle character(s) of the said string: th
# Original string: PHP
# Middle character(s) of the said string: H
# Original string: Java
# Middle character(s) of the said string: av

s=input()
n=len(s)
if n%2==0:
    print(s[n//2-1:n//2+1])
else:
    print(s[n//2])