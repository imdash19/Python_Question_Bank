# Reads a monetary amount and formats it as currency with dollar sign, commas for thousands, and two decimal places using f-string syntax. Modern approach to currency formatting.

amount = float(input())

print("${:,.2f}".format(amount))