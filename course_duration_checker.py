# Create Course class with duration attribute and print Long Course if duration >6 months

class Course:
    def __init__(self, duration):
        self.duration= duration

c= Course(float(input()))

if c.duration > 6:
    print('Long Course')

else:
    print('Short Course')
