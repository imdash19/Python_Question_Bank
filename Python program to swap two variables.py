# Write a Python program to swap two variables.

def swap_variables():
    a= input('Enter the first variable: ')
    b= input('Enter the second variable: ')
    a, b = b, a
    print("The new variable is: ", a)
    print("The new variable is: ", b)

swap_variables()