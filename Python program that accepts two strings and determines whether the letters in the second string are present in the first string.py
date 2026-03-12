# Write a Python program that accepts two strings and determines whether the letters in the second string are present in the first string.
# Sample Input:
# ["python", "ypth"]
# ["python", "ypths"]
# ["python", "ypthon"]
# ["123456", "01234"]
# ["123456", "1234"]
# Sample Output:
# True
# False
# True
# False
# True

s1=input("Enter first string: ")
s2=input("Enter second string: ")

print(all(ch in s1 for ch in s2))