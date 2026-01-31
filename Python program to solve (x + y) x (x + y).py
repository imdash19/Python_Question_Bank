# 	Write a Python program to solve (x + y) * (x + y).
# Test Data: x = 4, y = 3
# Expected Output: (4 + 3) ^ 2) = 49

def calculate_square():
    a= int(input("Enter a number: "))
    b= int(input("Enter another number: "))
    print(f'({a} + {b}) ^ 2 = {(a + b) ** 2}')

calculate_square()