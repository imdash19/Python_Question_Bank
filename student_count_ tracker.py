# Create a Student class.
# Use a class variable count to track the total students.
# Create a class method show_count that prints the total.
# Increment count manually when creating objects.

class Student:
    count = 0

    @classmethod
    def show_count(cls):
        print(cls.count)

student1 = Student()
Student.count += 1

student2 = Student()
Student.count += 1

student3 = Student()
Student.count += 1

Student.show_count()
