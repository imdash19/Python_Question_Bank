# This program demonstrates how to use super() with constructors in Python.
# Create a parent class Person with a constructor that accepts name and age.
# Create a child class Student.
# Use super() inside the child constructor to call the parent constructor.
# Create a method display_details() to print the name and age.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def display_details(self):
        print(self.name)
        print(self.age)

s = Student(input(), int(input()))
s.display_details()
