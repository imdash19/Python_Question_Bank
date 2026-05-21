# This program demonstrates how a child class can reuse parent class methods using inheritance.
# Create a parent class User with a method login() that prints a static message.
# Create a child class Admin that inherits from User.
# Create an Admin object and call the login() method using the child object.

class User:
    def login(self):
        print("User Logged In")

class Admin(User):
    pass

a = Admin()
a.login()
