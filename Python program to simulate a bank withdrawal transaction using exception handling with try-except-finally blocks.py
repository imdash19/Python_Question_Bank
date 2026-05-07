# Write a Python program to simulate a bank withdrawal transaction using exception handling with try-except-finally blocks.Here's what you need to do:
# Start with a predefined account balance of 5000.0 rupees stored in a variable.
# Take the withdrawal amount as input from the user.
# Use a try block to convert the input into a float number and attempt the withdrawal.
# If the user enters non-numeric input, catch the ValueError exception and display an error message.
# Inside the try block, check if the withdrawal amount is greater than the available balance.
# If the withdrawal amount exceeds the balance, raise a custom error for insufficient funds.
# If the withdrawal amount is zero or negative, display an error message.
# Use a finally block that always executes and prints "Transaction attempted" regardless of success or failure.
# If the withdrawal is successful, subtract the amount from the balance and display the updated balance.
# The program should handle all cases without crashing.
# Input Format:
# Single line contains the withdrawal amount which can be a number or non-numeric text.
# Output Format:
# Always print "Transaction attempted" from the finally block.
# If successful: Display "Withdrawal successful! Updated balance: [new_balance]".
# If insufficient funds: Display "Error: Insufficient funds".
# If zero or negative amount: Display "Error: Withdrawal amount must be positive".
# If non-numeric input: Display "Error: Invalid input. Please enter a numeric value".

class InsufficientBalanceError(Exception):
    pass

class ZeroNegativeError(Exception):
    pass

balance= 5000.0

try:
    amount= float(input())

    if amount > balance:
        raise InsufficientBalanceError

    if not balance > 0:
        raise ZeroNegativeError

except ValueError:
    print('Error: Invalid input. Please enter a numeric value')

except InsufficientBalanceError:
    print('Error: Insufficient funds')

except ZeroNegativeError:
    print("Error: Withdrawal amount must be positive")

else:
    print(f'Withdrawal successful! Updated balance: {balance-amount}')

finally:
    print('Transaction attempted')
