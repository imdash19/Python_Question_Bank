# Write a Python program to print a variable without spaces between values.
# Sample value: x =30
# Expected output: Value of x is "30"

def print_variable():
    x = int(input("Enter value of x: "))
    print(f'Value of x is "{x}"')
print_variable()