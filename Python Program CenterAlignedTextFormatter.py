# You need to create a program that formats text with center-alignment. Center-alignment means the text is placed in the middle, with spaces added equally on both the left and right sides to fill up the total width.
# Here's how it works:

# You have a text string that you want to display
# You have a specific width (total number of characters) for displaying the text
# The text should appear in the center of this width
# Empty spaces will be added on both left and right sides to fill the remaining width

# Example: If your text is "Hello" and width is 11, the output will be "   Hello   " (3 spaces on left, "Hello", 3 spaces on right)
# You need to create a program that:

# Takes a text string as input
# Takes the total width (number of characters) as input
# Displays the text center-aligned within that width using the traditional %-formatting method

# Input Format:

# First line: Text string (string)
# Second line: Total width for alignment (integer)

# Output Format:

# # Print the center-aligned text within the specified width

text = input()
width = int(input())

print("%s" % text.center(width))