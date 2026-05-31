# Reads a password from input while masking the displayed characters for security. The program typically shows asterisks or dots instead of the actual characters as the user types.

from getpass import getpass

password = getpass("Enter Password: ")

print("Password received successfully")
