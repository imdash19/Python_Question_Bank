# Write a Python program to set the indentation of the first line.

text = input("Enter multi-line text:\n")
indent = int(input("Enter number of spaces for indentation: "))

lines = text.split('\n')

if lines:
    lines[0] = ' ' * indent + lines[0]

result = '\n'.join(lines)

print("\nOutput:\n" + result)