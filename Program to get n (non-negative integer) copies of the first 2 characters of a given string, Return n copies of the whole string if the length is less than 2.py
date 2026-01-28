# Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string. Return n copies of the whole string if the length is less than 2.

def generate_copies(string, n):
    if len(string)==2:
        return string * n
    else:
        return string[:2] * 2

string= input("Enter a string: ")
n= int(input("Enter a number: "))

print(generate_copies(string, n))