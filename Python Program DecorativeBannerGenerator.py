# Beginner-Friendly Python Question

# 1. Problem Statement Description
# You need to create a program that makes a decorative text banner for announcements, titles, or certificates. A banner has a border on top and bottom with the text centered in the middle.
# Here's how it works:

# You have a text that you want to display as a banner (like "WELCOME" or "CONGRATULATIONS")
# You specify the total width of the banner
# You choose a border character (like *, =, -, or #) to decorate the top and bottom
# The program creates a beautiful 3-line banner:

# Line 1: Border character repeated across the full width
# Line 2: Your text centered with spaces on both sides
# Line 3: Border character repeated across the full width



# Example: Text = "PYTHON", Width = 20, Border = *
# ********************
#        PYTHON       
# ********************
# You need to create a program that:

# Takes the text to display
# Takes the total banner width
# Takes the border character
# Creates and displays a decorative 3-line banner

# Input Format:

# First line: Text for the banner (string)
# Second line: Total width of the banner (integer)
# Third line: Border character (single character like *, =, -, #)

# Output Format:

# Print the 3-line decorative banner with borders and centered text

text = input()
width = int(input())
border = input()

print(border * width)
print("{:^{}s}".format(text, width))
print(border * width)