# You are building a test score display system for students. The system stores accuracy scores as decimal values (like 0.92 for 92% correct answers), and you need to display them in a user-friendly percentage format.
# Here's how it works:

# You have a decimal value between 0 and 1 representing the accuracy ratio
# You need to convert this decimal to percentage format
# The percentage should be displayed with exactly 2 decimal places
# Add the % symbol at the end

# Example: If the decimal value is 0.7825, the output will be "78.25%"
# You need to create a program that:

# Takes a decimal value as input (between 0 and 1)
# Converts it to percentage format automatically
# Displays it with 2 decimal places and the % symbol using modern f-string syntax

# Input Format:

# Single line: A decimal value (float between 0 and 1)

# Output Format:

# Print the percentage with 2 decimal places followed by % symbol

accuracy = float(input())

print(f"{accuracy * 100:.2f}%")