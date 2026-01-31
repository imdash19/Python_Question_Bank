# Write a Python program that displays your name, age, and address on three different lines.

def print_address():
    name= input("Enter your name: ")
    age= int(input("Enter your age: "))
    address= input("Enter your address: ")
    print(f'{name} \n {age} \n {address}')