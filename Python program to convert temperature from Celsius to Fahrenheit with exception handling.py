# Write a Python program to convert temperature from Celsius to Fahrenheit with exception handling.
# Here's what you need to do:

# Take a temperature value in Celsius as input from the user.
# Use a try block to attempt converting the input to a float number.
# If the conversion is successful, apply the formula to convert Celsius to Fahrenheit: multiply the Celsius value by 9/5 and then add 32.
# Display the converted temperature in Fahrenheit with a clear message.
# Use an except block to catch ValueError when the user enters non-numeric input like letters or symbols.
# If the input is invalid, display an error message asking for a valid number.
# The program should not crash regardless of what the user enters.

# Input Format:

# Single line contains the temperature in Celsius which can be a number or non-numeric text.

# Output Format:

# If valid input: Display "Temperature in Fahrenheit: [value]".
# If invalid input: Display "Error: Invalid input. Please enter a valid number"

try:
    c= int(input())

except ValueError:
    print('Error: Invalid input. Please enter a valid number')

else:
    print(f'Temperature in Fahrenheit: {(c*(9/5)) + 32}')
