# Create a class Demo with:
# Public attribute public_data
# Private attribute __private_data
# Print both attributes:
# Public attribute can be accessed directly
# Private attribute must be accessed via a method

class Demo:
    def __init__(self):
        self.public_data= input()
        self.__private_data= input()

    def get_private_data(self):
        return self.__private_data

d= Demo
print(d.public_data, d.get_private_data())
