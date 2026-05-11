# Write a program that takes the lengths of three sides of a triangle as input in a single line separated by spaces. Calculate the semi-perimeter and then use Heron's formula to find the area of the triangle. The input will be three positive numbers separated by spaces, and the output should be a single number representing the area of the triangle
# Always write logic in a function + call it inside if __name__ == "__main__"

import math

def triangle_area(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

if __name__ == "__main__":
    a, b, c = map(float, input().split())
    print(triangle_area(a, b, c))
