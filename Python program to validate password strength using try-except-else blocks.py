# Write a Python program to validate password strength using try-except-else blocks.Here's what you need to do:
# Take a password as input from the user.
# Use a try block to get the password input and check if it is not empty by stripping whitespace.
# If the password is empty or contains only spaces, it should be considered invalid.
# Use an except block to catch any unexpected errors that might occur during input processing.
# Use an else block that executes only when the input is valid and not empty.
# Inside the else block, check if the password length is greater than or equal to 8 characters.
# If the password meets the length requirement, display "Strong password".
# If the password is shorter than 8 characters, display "Weak password: Password must be at least 8 characters long".
# Input Format:
# Single line contains the password as a string.
# Output Format:
# If password length >= 8: Display "Strong password".
# If password length < 8: Display "Weak password: Password must be at least 8 characters long".

try:
    password= input()
    password= password.strip()

    if not password:
        raise ValueError

except ValueError:
    print('Error: Invalid input. Please enter a valid number')

else:
    if len(password) >= 8:
        print('Strong password')
    else:
        print('Weak password: Password must be at least 8 characters long')
