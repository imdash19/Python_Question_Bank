# Write a Python program that determines whether a given number (accepted from the user) is even or odd, and prints an appropriate message to the user.

def check_even_odd(n):
    if n%2 == 0:
        return "Even"
    else:
        return "Odd"

n= int(input("Enter a number: "))
print(check_even_odd(n))