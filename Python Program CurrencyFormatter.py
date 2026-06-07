# Reads a monetary amount and formats it as currency with dollar sign, commas for thousands, and two decimal places using .format() method.

amount = float(input())

print("${:,.2f}".format(amount))