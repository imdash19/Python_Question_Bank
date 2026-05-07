# Write a Python program to perform division with multiple exception handling.Here's what you need to do:
# Take two numbers as input from the user on separate lines.
# The first number will be the dividend (the number to be divided).
# The second number will be the divisor (the number to divide by).
# Use a try block to attempt converting the inputs to integers and perform the division operation.
# If the division is successful, display the result in the format "Result: [answer]".
# Use an except block to catch ZeroDivisionError when the user tries to divide by zero and display "Error: Cannot divide by zero".
# Use another except block to catch ValueError when the user enters non-numeric input and display "Error: Invalid input. Please enter valid numbers".
# The program should handle all types of errors without crashing.
# Input Format:
# First line contains the dividend (can be a number or non-numeric text).
# Second line contains the divisor (can be a number or non-numeric text).
# Output Format:
# If division succeeds: Display "Result: [answer]".
# If divisor is zero: Display "Error: Cannot divide by zero".
# If non-numeric input: Display "Error: Invalid input. Please enter valid numbers".

try:
    n1, n2= int(input()), int(input())
    result= n1/n2

except ValueError:
    print('Error: Invalid input. Please enter valid numbers')

except ZeroDivisionError:
    print('Error: Cannot divide by zero')

else:
    print(f'Result: {result}')
