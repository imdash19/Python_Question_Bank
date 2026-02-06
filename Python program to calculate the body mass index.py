# Write a Python program to calculate the body mass index.

def calculate_bmi():
    weight = float(input("Enter your weight in kilograms (kg): "))
    height = float(input("Enter your height in meters (m): "))

    if weight <= 0 or height <= 0:
        print("Weight and height must be positive values.")
        return

    bmi = weight / (height ** 2)

    print("\nYour BMI is:", round(bmi, 2))

    if bmi < 18.5:
        print("Category: Underweight")
    elif 18.5 <= bmi < 24.9:
        print("Category: Normal weight")
    elif 25 <= bmi < 29.9:
        print("Category: Overweight")
    else:
        print("Category: Obese")

calculate_bmi()