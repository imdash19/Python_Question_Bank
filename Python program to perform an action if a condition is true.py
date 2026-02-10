# Write a Python program to perform an action if a condition is true.
# Given a variable name, if the value is 1, display the string "First day of a Month!" and do nothing if the value is not equal.

def check_first_day():
    value = int(input("Enter a value: "))

    if value == 1:
        print("First day of a Month!")

check_first_day()