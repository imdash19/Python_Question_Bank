# You are creating a grade calculator that shows a student's test score as a percentage. Teachers often record scores as decimal values (like 0.85 for 85%), and you need to convert and display them in a readable percentage format.
# Here's how it works:

# You have a decimal value between 0 and 1 (for example, 0.75 means 75%)
# You need to convert this decimal to a percentage format
# The percentage should be displayed with exactly 2 decimal places
# Add the % symbol at the end

# Example: If the decimal value is 0.856, the output will be "85.60%"
# You need to create a program that:

# Takes a decimal value as input (between 0 and 1)
# Converts it to percentage format (multiply by 100)
# Displays it with 2 decimal places and the % symbol using .format() method

# Input Format:

# Single line: A decimal value (float between 0 and 1)

# Output Format:

# Print the percentage with 2 decimal places followed by % symbol

score = float(input())

print("{:.2f}%".format(score * 100))