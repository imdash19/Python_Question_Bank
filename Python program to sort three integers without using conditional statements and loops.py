# Write a Python program to sort three integers without using conditional statements and loops.

def sort_three_numbers():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))

    smallest = min(a, b, c)
    largest = max(a, b, c)
    middle = a + b + c - smallest - largest

    print("\nSorted order:")
    print(smallest, middle, largest)

sort_three_numbers()