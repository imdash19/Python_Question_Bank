# Write a Python program to extract and display the name from a given Email address.
# Sample Data:
# ("ram@example.com") -> ("ram")
# ("kvr.java@example.com") -> ("kvr.java")
# ("fully-qualified-domain@hyd.com") -> ("fullyqualifieddomain")

email = input()

name = email.split('@')[0]
name = name.replace('-', '')

print(name)