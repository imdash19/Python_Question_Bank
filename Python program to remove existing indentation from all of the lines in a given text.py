# Write a Python program to remove existing indentation from all of the lines in a given text.

import textwrap

text = ""
while True:
    try:
        line = input()
        text += line + "\n"
    except EOFError:
        break

result = textwrap.dedent(text)

print(result)