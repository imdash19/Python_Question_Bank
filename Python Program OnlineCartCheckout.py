# You need to create a program that calculates the final amount to be paid at checkout in an online shopping cart.
# The program should:

# Take the cart amount as input
# Apply a 10% discount if the cart amount is greater than 1000
# If the amount is 1000 or less, no discount is applied
# Calculate and print the final payable amount

# Input Format:

# Single line: Cart amount (a number)

# Output Format:

# Print the final payable amount after applying discount (if applicable), rounded to 2 decimal places

class OnlineCartCheckout:
    def calculate_amount(self, amount):
        if amount > 1000:
            amount -= amount * 0.10

        print(f"{amount:.2f}")

amount = float(input())

o = OnlineCartCheckout()
o.calculate_amount(amount)
