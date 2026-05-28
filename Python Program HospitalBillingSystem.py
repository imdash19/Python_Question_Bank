# Beginner-Friendly Python Question

# 1. Problem Statement Description
# You are building a simple hospital billing system. The hospital needs to calculate the final bill for patients who have insurance coverage.
# Here's how it works:

# Every patient has an initial medical bill amount
# Some patients have insurance that can reduce their bill
# Important Rule: Insurance discount is only applied if the total bill is more than $5000
# If the bill is $5000 or less, the patient pays the full amount (no insurance discount)

# You need to create a program that:

# Takes the patient's name, their total bill amount, and their insurance coverage percentage
# Calculates the final bill after applying insurance (only if bill > 5000)
# Shows the final amount the patient needs to pay

# Input Format:

# First line: Patient's name (string)
# Second line: Total bill amount in dollars (float/integer)
# Third line: Insurance coverage percentage (integer, e.g., 20 means 20% coverage)

# Output Format:

# Print the final bill amount rounded to 2 decimal places

class HospitalBillingSystem:
    def calculate_bill(self, name, bill_amount, insurance_percent):
        if bill_amount > 5000:
            discount = bill_amount * insurance_percent / 100
            bill_amount -= discount

        print(f"{bill_amount:.2f}")

name = input()
bill_amount = float(input())
insurance_percent = int(input())

h = HospitalBillingSystem()
h.calculate_bill(name, bill_amount, insurance_percent)
