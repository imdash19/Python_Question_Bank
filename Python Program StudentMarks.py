# Create a class named StudentMarks with a method total_marks().
# If two marks are passed to the method, calculate and display the total marks.
# If three marks are passed to the method, calculate and display both the total marks and the average marks.

class StudentMarks:
    def total_marks(self, *marks):
        total = sum(marks)

        if len(marks) == 2:
            print(total)

        elif len(marks) == 3:
            average = total / 3
            print(total)
            print(f"{average:.2f}")

s = StudentMarks()

n = int(input())

if n == 2:
    m1 = int(input())
    m2 = int(input())
    s.total_marks(m1, m2)

elif n == 3:
    m1 = int(input())
    m2 = int(input())
    m3 = int(input())
    s.total_marks(m1, m2, m3)
