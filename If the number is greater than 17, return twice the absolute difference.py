# If the number is greater than 17, return twice the absolute difference.

def absolute_difference(num1, num2):
    return abs(num1-num2)

num1 = float(input('Please enter your first number: '))
num2 = float(input('Please enter your second number: '))
print(absolute_difference(num1, num2))