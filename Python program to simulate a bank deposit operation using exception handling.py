# Write a Python program to simulate a bank deposit operation using exception handling.Here's what you need to do:
# Start with a predefined account balance of 5000.0 rupees stored in a variable.
# Ask the user to enter the amount they want to deposit into their account.
# Use a try block to convert the user's input into a float number.
# If the user enters something that is not a number, catch the ValueError exception and display an error message.
# Use an else block that runs only when the input is successfully converted to a number.
# Inside the else block, check if the deposit amount is greater than zero.
# If the amount is positive, add it to the current balance and display the updated balance.
# If the amount is zero or negative, display an error message saying the deposit amount must be positive.
# Make sure the program handles all cases smoothly without crashing.
# Input Format:
# Single line contains the deposit amount which can be a number or non-numeric text.
# Output Format:
# If deposit is successful: Display "Deposit successful! Updated balance: [new_balance]".
# If amount is zero or negative: Display "Error: Deposit amount must be positive".
# If non-numeric input: Display "Error: Invalid input. Please enter a numeric value".

try:
    balance= 5000.0
    amount= float(input())

except IndexError:
    print('Error: Index out of range')

except ValueError:
    print('Error: Invalid input. Please enter a numeric value')

else:
    if amount > 0:
        print(f'Deposit successful! Updated balance: {balance+amount}')
    else:
        print('Error: Deposit amount must be positive')
