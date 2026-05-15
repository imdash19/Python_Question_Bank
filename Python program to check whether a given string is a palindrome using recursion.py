# Write a program to check whether a given string is a palindrome using recursion. 
# The program should compare the first and last characters. 
# If they are equal, recursion continues with the remaining substring. 
# The process stops when the string length is 0 or 1. 
# Output should be TRUE or FALSE.

def is_palindrome(text):
    if len(text) <= 1:
        return True

    if text[0] != text[-1]:
        return False

    return is_palindrome(text[1:-1])

string = input("Enter a string: ")

if is_palindrome(string):
    print("TRUE")
else:
    print("FALSE")
