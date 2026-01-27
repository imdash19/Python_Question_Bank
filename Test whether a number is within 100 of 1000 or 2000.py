# Write a Python program to test whether a number is within 100 or 1000 or 2000.

def check_range(num):
    if num < 100:
        return print('It is within 100')

    elif num < 1000:
        return print('It is within 1000')

    elif num < 2000:
        return print('It is within 2000')

    else:
        return print('It is above 2000')

num= float(input('Please enter a number: '))
check_range(num)