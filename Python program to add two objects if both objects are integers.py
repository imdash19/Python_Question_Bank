# Write a Python program to add two objects if both objects are integers.

def add_if_integers():
    a= input("Enter first number: ")
    b= input("Enter second number: ")

    if a.lstrip('-').isdigit() and b.lstrip('-').isdigit():
        return a+b
    return "Both objects must be integers"

print(add_if_integers())