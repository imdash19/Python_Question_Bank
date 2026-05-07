# Write a Python program to accept age from the user and validate it using exception handling.Here's what you need to do:
# Take an age value as input from the user.
# The program should handle cases where the user enters non-numeric values like letters or symbols.
# The program should also check if the age is negative and display an appropriate error message.
# If the input is valid and the age is a positive number, display the entered age.
# Use try-except blocks to handle exceptions and prevent the program from crashing.
# Display clear error messages for different types of invalid inputs.
# Input Format:
# Single line contains the age value which can be a number, negative number, or non-numeric text.
# Output Format:
# If valid positive age: Display "Valid age: [age]".
# If negative age: Display "Error: Age cannot be negative".
# If non-numeric input: Display "Error: Please enter a valid number".

class NegativeAgeError(Exception):
    pass

try:
    age = int(input())
    if age < 0:
        raise NegativeAgeError

except ValueError as e:
    print("Error: Please enter a valid number")

except NegativeAgeError:
    print("Error: Age cannot be negative")
    
else:
    print(f"Valid age: {age}")
