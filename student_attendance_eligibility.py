# Create Student class with attendance attribute and print Eligible if >=75 else Not Eligible

class Student:
    def __init__(self, attendance):
        self.attendance = attendance

attendance = int(input())

student = Student(attendance)

if student.attendance >= 75:
    print("Eligible")
else:
    print("Not Eligible")
