# Write a Python program to display formatted text (width=50) as output.

import textwrap

text = input()

formatted = textwrap.fill(text, width=50)

print(formatted)