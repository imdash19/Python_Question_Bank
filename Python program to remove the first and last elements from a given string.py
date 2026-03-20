# Write a Python program to remove the first and last elements from a given string.
# Original string: PHP
# Removing the first and last elements from the said string: H
# Original string: Python
# Removing the first and last elements from the said string: ytho
# Original string: JavaScript
# Removing the first and last elements from the said string: avaScrip

def remove_first_and_last_elements():
    s= input()
    print(s[1:len(s)-1])
    return
remove_first_and_last_elements()