# Create a parent class Shape with method area(). 
# Create a child class Rectangle that overrides area() to calculate area using length and breadth.

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def area(self, length, breadth):
        print(length * breadth)

length = float(input())
breadth = float(input())

r = Rectangle()
r.area(length, breadth)
