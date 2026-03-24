# Write a Python program to find the largest and smallest digits of a given number.
# Original Number: 9387422
# Largest Digit of the said number: 9
# Smallest Digit of the said number: 2
# Original Number: 500
# Largest Digit of the said number: 5
# Smallest Digit of the said number: 0
# Original Number: 231548
# Largest Digit of the said number: 8
# Smallest Digit of the said number: 1

def find_digits(n):
    digits = list(map(int, str(n)))

    largest = max(digits)
    smallest = min(digits)

    print("Original Number:", n)
    print("Largest Digit of the said number:", largest)
    print("Smallest Digit of the said number:", smallest)


find_digits(int(input()))