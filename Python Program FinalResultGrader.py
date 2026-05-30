# Create a parent class Result with a method calculate_grade(marks).
# Create a child class FinalResult that overrides calculate_grade() using if-else conditions to assign grades.

class Result:
    def calculate_grade(self, marks):
        pass

class FinalResult(Result):
    def calculate_grade(self, marks):
        if marks >= 90:
            print("A")
        elif marks >= 75:
            print("B")
        elif marks >= 50:
            print("C")
        else:
            print("F")

marks = float(input())

f = FinalResult()
f.calculate_grade(marks)
