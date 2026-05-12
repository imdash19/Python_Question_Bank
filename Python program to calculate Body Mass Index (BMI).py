# Write a program to calculate Body Mass Index (BMI). 
# The program should accept two space-separated lists: weights and heights.
# BMI should be calculated using the formula weight/(height²).
# Python’s map() function should process both lists together.
# The output should be rounded to two decimals.

weights = list(map(float, input("Enter weights: ").split()))
heights = list(map(float, input("Enter heights: ").split()))

bmi = list(map(lambda w, h: round(w / (h ** 2), 2), weights, heights))

print(bmi)
