# Create a User class with a private attribute __password.
# Use a method to verify the password:
# Print "Access Granted" if input matches __password
# Print "Access Denied" otherwise

class User:
    def __init__(self, password):
        self.__password= password

    def check_access(self, password):
        if password == self.password:
            return 'Access Granted'

        else:
            return 'Access Denied'

u= User(input())
print(u.check_access(input()))
