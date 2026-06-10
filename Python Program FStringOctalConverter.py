# Perfect! Let me create the beginner-friendly version:

# 1. Problem Statement Description
# You need to create a program that converts a decimal (base-10) number to octal (base-8) format using modern Python syntax.
# The program should:

# Take an integer as input
# Convert and display it in octal format using f-string (base-8 number system that uses digits 0-7)

# For example, decimal number 15 becomes 17 in octal.
# Input Format:

# Single line: An integer number

# Output Format:

# Print the number in octal format (without any prefix like 0o)

number = int(input())

print(f"{number:o}")
