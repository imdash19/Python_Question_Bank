# Create a Course class with attributes:
# -> course_name
# -> duration
# Create an object of the class.
# Print the values of the attributes.

class Course:
    def __init__(self, course_name, duration):
        self.course_name= course_name
        self.duration= duration

c= Course(input(), int(input()))
print(c.course_name)
print(c.duration)
