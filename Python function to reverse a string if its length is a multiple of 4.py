# Write a Python function to reverse a string if its length is a multiple of 4.

def reverse_string(s):
    return s[::-1]

s= input()
if len(s)%4==0:
    reverse_string(s)