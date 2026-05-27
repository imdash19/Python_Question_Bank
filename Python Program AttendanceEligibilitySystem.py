# Create base class Student with method get_attendance(). 
# Create child class Eligibility that checks eligibility using if condition. 
# Create another child class Result that prints Eligible or Not Eligible.

class Student:
    def get_attendance(self):
        self.attendance = int(input())

class Eligibility(Student):
    def check_eligibility(self):
        if self.attendance >= 75:
            self.result = "Eligible"
        else:
            self.result = "Not Eligible"

class Result(Eligibility):
    def display_result(self):
        print(self.result)

r = Result()
r.get_attendance()
r.check_eligibility()
r.display_result()
