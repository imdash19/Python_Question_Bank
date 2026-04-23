# Write a Python program to lowercase the first n characters in a string.

text = input("Enter a string: ")
n = int(input("Enter number of characters to lowercase: "))

result = text[:n].lower() + text[n:]

print(result)