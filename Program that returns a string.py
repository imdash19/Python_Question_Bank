# Write a Python program that returns a string that is n (non-negative integer) copies of a given string.

def string_copies(text, n):
    if n < 0:
        return "n must be a non-negative integer"
    return text * n

text = input("Enter a string: ")
n = int(input("Enter number of copies: "))

result = string_copies(text, n)
print("Result:", result)