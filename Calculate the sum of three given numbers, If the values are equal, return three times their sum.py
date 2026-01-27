# Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum

def calculate_sum_three(num1, num2, num3):
    if num1 == num2 and num1 == num3:
        return num1*3, num2*3, num3*3
    else:
        return num1+num2+num3

num1= float(input('Please enter first number: '))
num2= float(input('Please enter second number: '))
num3= float(input('Please enter third number: '))
print(calculate_sum_three(num1, num2, num3))