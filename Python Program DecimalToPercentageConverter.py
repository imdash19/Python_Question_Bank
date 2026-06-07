# You need to create a program that converts a decimal number to percentage format with proper formatting.The program should:

# Take a decimal value between 0 and 1 as input (for example, 0.75 represents 75%)
# Convert it to percentage by multiplying by 100
# Display the result with exactly 2 decimal places followed by the % symbol
# Input Format:

# Single line: A decimal number between 0 and 1
# Output Format:

# Print the percentage value with 2 decimal places followed by % symbol (example: 75.00%)

value = float(input())

print(f"{value * 100:.2f}%")