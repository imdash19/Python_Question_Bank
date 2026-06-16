# You need to create a program that converts a decimal (base-10) number to hexadecimal (base-16) format using the traditional formatting method.
# The program should:

# Take an integer as input
# Convert and display it in hexadecimal format using %-formatting operator (base-16 number system that uses digits 0-9 and letters a-f)

# For example, decimal number 255 becomes ff in hexadecimal.
# Input Format:

# Single line: An integer number

# Output Format:

# Print the number in lowercase hexadecimal format (without any prefix like 0x)

number = int(input())

print("%x" % number)
