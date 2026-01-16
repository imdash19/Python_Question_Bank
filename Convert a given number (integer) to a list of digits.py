# 	Write a Python program to convert a given number (integer) to a list of digits.
# Sample Output: [1, 2, 3]
#     [1, 3, 4, 7, 8, 2, 3]

num = int(input("Enter a number: "))
digits = [int(i) for i in str(num)]
print(digits)