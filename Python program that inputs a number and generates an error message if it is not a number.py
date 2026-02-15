# Write a Python program that inputs a number and generates an error message if it is not a number.

def check_number():
    user_input = input("Enter a number: ")

    try:
        number = float(user_input)
        print("Valid number entered:", number)
    except ValueError:
        print("Error: The input is not a valid number.")
check_number()