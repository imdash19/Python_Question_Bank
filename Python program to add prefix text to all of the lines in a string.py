# Write a Python program to add prefix text to all of the lines in a string

text = input("Enter multi-line text:\n")
prefix = input("Enter prefix: ")

lines = text.split('\n')
result = '\n'.join(prefix + line for line in lines)

print("\nOutput:\n" + result)