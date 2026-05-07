# Write a Python program to convert temperature from Celsius to Fahrenheit using exception handling with try-except-finally blocks.Here's what you need to do:
# Take a temperature value in Celsius as input from the user.
# Use a try block to convert the input into a float number.
# If the user enters non-numeric input like letters or symbols, catch the ValueError exception and display an error message.
# If the conversion is successful, apply the formula to convert Celsius to Fahrenheit: F = (C × 9/5) + 32.
# Display the converted temperature in Fahrenheit clearly.
# Use a finally block that always executes and prints "Input processed" regardless of whether the conversion succeeded or failed.
# The finally block ensures that cleanup or logging operations happen in all cases.
# The program should handle both valid numeric inputs and invalid non-numeric inputs gracefully.
# Input Format:
# Single line contains the temperature in Celsius which can be a number or non-numeric text.
# Output Format:
# Always print "Input processed" from the finally block.
# If valid input: Display "[celsius]°C is equal to [fahrenheit]°F".
# If invalid input: Display "Error: Invalid input. Please enter a numeric value".

try:
    c= float(input())

except ValueError:
    print('Error: Invalid input. Please enter a numeric value')

else:
    print(f'{c}°C is equal to {(c*(9/5))+32}°F')

finally:
    print('Input processed')
