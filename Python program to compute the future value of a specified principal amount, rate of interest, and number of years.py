# Write a Python program to compute the future value of a specified principal amount, rate of interest, and number of years.
# Test Data: amt = 10000, int = 3.5, years = 7
# Expected Output: 12722.79

def calculate_future_value():
    p= float(input('Enter principle amount: '))
    t= int(input('Enter number of years: '))
    r= float(input('Enter rate of interest: '))
    return p * ((1 + r / 100) ** t)

print(calculate_future_value())