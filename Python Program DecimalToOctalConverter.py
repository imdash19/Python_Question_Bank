# You need to create a program that converts a decimal (base-10) number to octal (base-8) format.
# The program should:

# Take an integer as input
# Convert and display it in octal format (base-8 number system that uses digits 0-7)

# For example, decimal number 10 becomes 12 in octal.
# Input Format:

# Single line: An integer number

# Output Format:

# Print the number in octal format (without any prefix like 0o)

number = int(input())

print("{:o}".format(number))
