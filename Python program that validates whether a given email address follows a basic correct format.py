# Create a program that validates whether a given email address follows a basic correct format. An email address is considered valid if it contains three essential parts: characters before the @ symbol (username), the @ symbol itself, and a domain name after the @ symbol (like gmail.com or yahoo.com).For this exercise, we are implementing a simple email validator that checks the basic structure. A valid email should have at least one character before the @, followed by the @ symbol, and then a domain name that contains at least one dot (.) separating the domain name and extension. For example, "user@example.com" is valid, but "userexample.com" or "@example.com" are invalid.You will use regular expressions to create a pattern that matches this email structure and validate the user's input against this pattern.Input Format:

# A single line containing an email address to be validated
# Output Format:

# Print "Valid email" if the email follows the correct format
# Print "Invalid email" if the email does not meet the requirements

import re

email = input()

pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

if re.fullmatch(pattern, email):
    print("Valid email")
else:
    print("Invalid email")
